# Threat Report: Twitter Phishing Campaign
**Report ID:** THREAT-20250619-001  
**Date:** 2025-06-19  
**Analyst:** Jasti Jagadish Babu  
**Severity:** HIGH  
**Status:** Documented

---

## Executive Summary

A phishing campaign was detected on Twitter (X) using fake account verification messages directing users to a credential harvesting page mimicking a financial institution's login portal.

---

## Threat Indicators

| Indicator | Type | Description |
|-----------|------|-------------|
| `http://paypa1-verify.xyz/login` | Malicious URL | Typosquatted PayPal domain |
| `@PayPa1_Support` | Fake Account | Impersonating PayPal support |
| "Your account is suspended" | Phishing Phrase | Urgency-based social engineering |

---

## Attack Chain

1. **Initial Contact** — Victim receives a DM from fake support account
2. **Urgency Trigger** — Message warns of account suspension
3. **Redirect** — Shortened URL redirects to phishing page
4. **Credential Harvest** — Fake login form captures username + password
5. **Account Takeover** — Attacker accesses victim's real account

---

## OSINT Findings

- Domain registered 3 days before campaign started
- Hosting provider: Shared hosting in Eastern Europe
- SSL certificate: Let's Encrypt (30-day), auto-renewed

---

## Recommended Actions

- [ ] Report account `@PayPa1_Support` to Twitter
- [ ] Submit domain to PhishTank and VirusTotal
- [ ] Alert PayPal security team
- [ ] Notify followers in affected threads

---

## MITRE ATT&CK Mapping

| Technique | ID | Description |
|-----------|-----|-------------|
| Spearphishing via Social Media | T1566.003 | DM-based phishing |
| Credential Phishing | T1056 | Fake login page |
| Impersonation | T1656 | Fake brand account |

---

*Report generated for educational/research purposes only.*
