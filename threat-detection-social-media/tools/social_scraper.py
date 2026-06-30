#!/usr/bin/env python3
"""
Social Media Scraper for Threat Detection
Author: Jasti Jagadish Babu
Purpose: Collect public posts/data from social media for threat analysis
"""

import requests
import json
import time
import re
from datetime import datetime

TARGET_KEYWORDS = [
    "free giveaway click here",
    "your account has been compromised",
    "verify your identity now",
    "limited time offer login",
    "claim your prize",
    "DM for details",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; ThreatBot/1.0; +https://github.com/jagadish-sec)"
}


def extract_urls(text: str) -> list:
    url_pattern = r"https?://[^\s]+"
    return re.findall(url_pattern, text)


def scan_post_for_threats(post_text: str) -> dict:
    result = {
        "timestamp": datetime.utcnow().isoformat(),
        "post_snippet": post_text[:120],
        "urls_found": extract_urls(post_text),
        "keyword_matches": [],
        "threat_level": "LOW",
        "flags": []
    }
    post_lower = post_text.lower()
    for keyword in TARGET_KEYWORDS:
        if keyword.lower() in post_lower:
            result["keyword_matches"].append(keyword)
            result["flags"].append(f"Suspicious keyword: '{keyword}'")
    if len(result["urls_found"]) > 2:
        result["flags"].append("Multiple URLs detected in single post")
    if len(result["keyword_matches"]) >= 3 or len(result["urls_found"]) > 3:
        result["threat_level"] = "HIGH"
    elif len(result["keyword_matches"]) >= 1 or len(result["urls_found"]) > 1:
        result["threat_level"] = "MEDIUM"
    return result


if __name__ == "__main__":
    demo_post = "URGENT: Your account has been compromised! Click here to verify: http://phish.example.com/login"
    result = scan_post_for_threats(demo_post)
    print(json.dumps(result, indent=2))
