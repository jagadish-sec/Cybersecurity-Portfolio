# Case Studies: Social Media Threats

## Case 1: Twitter Crypto Scam (Bitcoin Giveaway)

**Type:** Financial Scam  
**Platform:** Twitter  
**Severity:** HIGH

### Description
Attackers compromised high-profile accounts and posted fake Bitcoin giveaway messages directing users to send BTC to receive double back.

### TTPs Used
- Account takeover via SIM swapping + phishing
- Urgency and authority (impersonating known figures)
- Cryptocurrency irreversibility exploited

### Lessons Learned
- Enable 2FA on all accounts
- Verify cryptocurrency addresses through official channels
- Be skeptical of too-good-to-be-true offers

---

## Case 2: LinkedIn Spearphishing

**Type:** Spearphishing  
**Platform:** LinkedIn  
**Severity:** CRITICAL

### Description
Fake recruiters created convincing LinkedIn profiles and sent malicious job offer PDFs containing macros targeting cybersecurity professionals.

### TTPs Used
- T1566.002 — Spearphishing Attachment
- Fake job lure social engineering
- Macro-embedded PDF

### Lessons Learned
- Verify recruiter identity independently
- Disable macros in Office by default
- Use EDR on corporate endpoints

---

## Case 3: Instagram Phishing via DM

**Type:** Credential Phishing  
**Platform:** Instagram  
**Severity:** MEDIUM

### Description
Fake Instagram Security accounts sent DMs claiming accounts would be deleted unless users verified via an external credential-harvesting link.

### Indicators
- `instagram-security-verify.com` (malicious domain)
- `@Instagram_Security_Help` (fake account)

---

## Key Takeaways

1. Attackers exploit urgency, authority, and fear
2. URL shorteners and typosquatting are common evasion tactics
3. Account age and behavior are strong threat signals
4. OSINT can reveal campaign infrastructure quickly
5. Always verify via official channels — never through DM links
