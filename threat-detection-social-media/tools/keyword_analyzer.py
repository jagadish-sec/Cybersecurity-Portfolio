#!/usr/bin/env python3
"""
Keyword Analyzer for Social Media Threat Detection
Author: Jasti Jagadish Babu
Purpose: Analyze text data for threat-indicating keywords and patterns
"""

import re
import argparse
import json

PHISHING_PATTERNS = [
    r"click here.{0,20}(verify|confirm|update|secure)",
    r"your (account|password|card).{0,20}(expire|suspend|block|comprom)",
    r"(win|won|prize|reward|gift).{0,30}(claim|collect|free)",
    r"(urgent|immediate|action required)",
    r"(login|sign.?in).{0,20}(now|immediately|asap)",
    r"(bit\.ly|tinyurl|goo\.gl)/[a-zA-Z0-9]+",
]

SOCIAL_ENGINEERING_PATTERNS = [
    r"(dm|direct message).{0,20}(detail|info|more)",
    r"(only|limited).{0,20}(slots|spots|time|offer)",
    r"(100%|guaranteed).{0,20}(free|safe|legit)",
    r"send.{0,20}(money|btc|crypto|gift card)",
]


def analyze_text(text: str) -> dict:
    text_lower = text.lower()
    matches = {"phishing": [], "social_engineering": [], "risk_score": 0}
    for pattern in PHISHING_PATTERNS:
        found = re.findall(pattern, text_lower)
        if found:
            matches["phishing"].append({"pattern": pattern, "matches": str(found)})
            matches["risk_score"] += 2
    for pattern in SOCIAL_ENGINEERING_PATTERNS:
        found = re.findall(pattern, text_lower)
        if found:
            matches["social_engineering"].append({"pattern": pattern, "matches": str(found)})
            matches["risk_score"] += 1
    if matches["risk_score"] >= 5:
        matches["classification"] = "HIGH RISK"
    elif matches["risk_score"] >= 2:
        matches["classification"] = "MEDIUM RISK"
    else:
        matches["classification"] = "LOW RISK"
    return matches


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Social Media Keyword Threat Analyzer")
    parser.add_argument("--input", help="Input text file")
    parser.add_argument("--text", help="Single text string to analyze")
    args = parser.parse_args()
    if args.text:
        print(json.dumps(analyze_text(args.text), indent=2))
    else:
        samples = [
            "URGENT: Your account will be suspended! Click here to verify now!",
            "Hey, DM me for more details on this limited time free offer!",
            "Good morning everyone, hope you have a great day!",
        ]
        for s in samples:
            print(f"\nText: {s}")
            print(json.dumps(analyze_text(s), indent=2))
