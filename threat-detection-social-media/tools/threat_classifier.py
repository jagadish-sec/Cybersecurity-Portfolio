#!/usr/bin/env python3
"""
Threat Classifier for Social Media Intelligence
Author: Jasti Jagadish Babu
Purpose: Classify detected threats by type, severity, and recommended action
"""

import json
from dataclasses import dataclass, asdict
from typing import Optional
from datetime import datetime


@dataclass
class ThreatReport:
    id: str
    timestamp: str
    platform: str
    content_snippet: str
    threat_type: str
    severity: str
    indicators: list
    recommended_action: str
    analyst_notes: Optional[str] = None


THREAT_RULES = {
    "PHISHING": {
        "keywords": ["verify", "login", "password", "account", "suspended", "click here"],
        "severity": "HIGH",
        "action": "Report to platform + block domain + alert users"
    },
    "MALWARE_DISTRIBUTION": {
        "keywords": ["download", "crack", "keygen", "free software", "exe", "apk"],
        "severity": "CRITICAL",
        "action": "Submit URL to VirusTotal + notify CERT + document IOCs"
    },
    "SCAM": {
        "keywords": ["giveaway", "free money", "prize", "won", "gift card", "bitcoin"],
        "severity": "MEDIUM",
        "action": "Report to platform abuse team + document account"
    },
    "IMPERSONATION": {
        "keywords": ["official account", "support team", "admin", "verified"],
        "severity": "HIGH",
        "action": "Report fake account + alert target organization"
    },
    "DOXXING": {
        "keywords": ["home address", "phone number", "personal info", "exposed", "leaked"],
        "severity": "CRITICAL",
        "action": "Immediate report + legal consultation + notify victim"
    },
}


def classify_threat(post_text: str, platform: str = "Unknown") -> ThreatReport:
    text_lower = post_text.lower()
    matched_type = "UNKNOWN"
    matched_indicators = []
    max_severity = "LOW"
    severity_order = {"LOW": 0, "MEDIUM": 1, "HIGH": 2, "CRITICAL": 3}
    for threat_type, rules in THREAT_RULES.items():
        hits = [kw for kw in rules["keywords"] if kw in text_lower]
        if hits:
            if severity_order[rules["severity"]] > severity_order.get(max_severity, 0):
                max_severity = rules["severity"]
                matched_type = threat_type
                matched_indicators = hits
    action = THREAT_RULES.get(matched_type, {}).get("action", "Document and monitor")
    return ThreatReport(
        id=f"THREAT-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
        timestamp=datetime.utcnow().isoformat(),
        platform=platform,
        content_snippet=post_text[:150],
        threat_type=matched_type,
        severity=max_severity,
        indicators=matched_indicators,
        recommended_action=action
    )


if __name__ == "__main__":
    samples = [
        ("Your PayPal account is suspended. Login here to verify: http://paypal-verify.phish.xyz", "Twitter"),
        ("Download FREE Photoshop crack! Get the keygen exe now!", "Telegram"),
        ("FREE Bitcoin giveaway! Send 0.01 BTC and get 0.1 back!", "Instagram"),
    ]
    reports = []
    for text, platform in samples:
        report = classify_threat(text, platform)
        reports.append(asdict(report))
        print(f"[{report.severity}] {report.threat_type} on {platform}")
    print(json.dumps(reports, indent=2))
