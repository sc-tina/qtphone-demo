# Android Cloud Device Demo - Cloud Android Device Management Scripts

> Tools for managing and monitoring **cloud Android devices** with dedicated IPs, built for
> social media automation, mobile app testing, multi-instance gaming, and fleet operations.

---

## Overview

This repository contains production-ready Python scripts demonstrating key capabilities
of any Android cloud device platform — IP verification, device health monitoring,
and fleet-wide batch auditing.

## Scripts

| File | Description |
|------|-------------|
| `ip_check.py` | Verify your cloud device's public IP address |
| `device_status_checker.py` | Real-time device health: screen, battery, network, apps, IP |
| `fleet_ip_audit.py` | Batch IP verification across your entire device fleet |

## Quick Start

```bash
# Verify device public IP
python ip_check.py

# Check device health status
python device_status_checker.py

# Audit IP pool across all fleet devices
python fleet_ip_audit.py
```

## Sample Output

```
=== Android Cloud Device Fleet IP Audit ===
Scanning 5 devices...
Device-01 | 203.0.113.42 | HK    | Status: UNIQUE
Device-02 | 198.51.100.17 | US-CA | Status: UNIQUE
Device-03 | 203.0.113.42 | HK    | Status: DUPLICATE
Device-04 | 192.0.2.88    | SG    | Status: UNIQUE
Device-05 | 203.0.113.42 | HK    | Status: DUPLICATE
Fleet Size: 5 | Unique IPs: 3 | Duplicates: 2
```

## Use Cases

| Use Case | Why Cloud Android Devices |
|----------|--------------------------|
| Social media automation | Run many accounts, each on its own isolated IP |
| Mobile app testing | Test across real Android devices with real geolocations |
| Multi-instance gaming | Parallel sessions without hardware or ban risk |
| Fleet management | Monitor status of all cloud devices from one terminal |
| Ad verification | Check ads from real device IPs in target regions |

## Ecosystem

Related open-source projects in the Android cloud device ecosystem:

- [integrity-checker](https://github.com/luoshixin93-sudo/integrity-checker) — SafetyNet + Play Integrity + CTS profile audit
- [cloudphone-sdk-python](https://github.com/luoshixin93-sudo/cloudphone-sdk-python) — Python SDK for Android cloud device APIs
- [stealth-browser-runner](https://github.com/luoshixin93-sudo/stealth-browser-runner) — Stealth Playwright browser runner
- [stealth-proxy-runner](https://github.com/luoshixin93-sudo/stealth-proxy-runner) — Headless stealth browser with proxy rotation

## Technologies Used

- Python 3.8+
- `requests` / `urllib` for HTTP APIs
- Android Debug Bridge (ADB) compatible

---

*Star the repo if you find it useful. Issues and PRs welcome!*
