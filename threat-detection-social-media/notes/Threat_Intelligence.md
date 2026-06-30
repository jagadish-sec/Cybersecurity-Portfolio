# Threat Intelligence Notes

## Threat Intelligence Lifecycle

1. **Planning** — Define requirements, target platforms, threat actors
2. **Collection** — Gather raw data (posts, profiles, URLs, IPs)
3. **Processing** — Parse, normalize, deduplicate data
4. **Analysis** — Identify TTPs, patterns, IOCs
5. **Dissemination** — Share in STIX/TAXII, reports, alerts
6. **Feedback** — Improve collection based on results

## Indicators of Compromise (IOCs) Types

| IOC Type | Example | Volatility |
|----------|---------|------------|
| IP Address | 192.168.1.1 | High |
| Domain | phish-example.com | Medium |
| URL | http://evil.com/login | High |
| Hash (MD5/SHA) | d41d8cd9... | Low |
| Email | attacker@evil.com | Medium |
| Username | @FakeSupp0rt | High |

## Social Media Threat Actor Categories

### Cybercriminals
- Financially motivated
- Phishing, scams, fraud

### Nation-State Actors
- Disinformation campaigns
- Targeted spearphishing

### Hacktivists
- Ideologically motivated
- Doxxing, DDoS threats

## MITRE ATT&CK for Social Media Threats

- **T1566.003** — Spearphishing via Social Media
- **T1656** — Impersonation
- **T1593** — Search Open Websites / Domains
- **T1598** — Phishing for Information
- **T1589** — Gather Victim Identity Information

## Threat Feeds & Resources

- [PhishTank](https://www.phishtank.com/)
- [AbuseIPDB](https://www.abuseipdb.com/)
- [VirusTotal](https://www.virustotal.com/)
- [URLhaus](https://urlhaus.abuse.ch/)
- [AlienVault OTX](https://otx.alienvault.com/)
