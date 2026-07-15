# Android Cloud Device Demo - Global Independent IP Android Android Cloud Phone

> **Live Demo Repository** | [android-cloud-device.com](https://www.android-cloud-device.com/) | [Main Repo](https://github.com/luoshixin93-sudo/android-cloud-device)

Android Cloud Device provides **cloud Android devices with dedicated, independent IPs** -- built for
social-media marketing, automation, gaming multi-instance, and large-scale app testing.

---

## What this repo shows

This repo demonstrates four Android Cloud Device core capabilities:

| Script | What it does |
|--------|-------------|
| ip_check.py | Verify your cloud device's public IP address |
| device_status_checker.py | Real-time device health: screen, battery, network, apps, IP |
| fleet_ip_audit.py | Batch IP verification across your entire device fleet |

## What's new (2026-07-14)

Four new open-source repos joined the Android Cloud Device ecosystem today:

| Repo | Description |
|------|-------------|
| [integrity-checker](https://github.com/luoshixin93-sudo/integrity-checker) | Android device integrity audit CLI (SafetyNet + Play Integrity API + CTS profile) |
| [play-integrity-helper](https://github.com/luoshixin93-sudo/play-integrity-helper) | One-click Play Integrity fix helper for cloud Android devices |
| [cloud-phone-gms-guide](https://github.com/luoshixin93-sudo/cloud-phone-gms-guide) | Step-by-step GMS/Google Play Store installation on cloud phones |
| [appium-parallel-runner](https://github.com/luoshixin93-sudo/appium-parallel-runner) | Parallel Appium test runner for Android/iOS real devices |

## Full Android Cloud Device Open-Source Ecosystem

15 open-source repos covering every layer of cloud Android infrastructure:

**Core Platform**
- [android-cloud-device](https://github.com/luoshixin93-sudo/android-cloud-device) - Main platform repo
- [cloudphone-sdk-python](https://github.com/luoshixin93-sudo/cloudphone-sdk-python) - Python SDK

**Testing & Automation**
- [appium-parallel-runner](https://github.com/luoshixin93-sudo/appium-parallel-runner) - Parallel Appium test runner
- [maestro-mobile-runner](https://github.com/luoshixin93-sudo/maestro-mobile-runner) - Fast Maestro UI test runner
- [stealth-browser-runner](https://github.com/luoshixin93-sudo/stealth-browser-runner) - Playwright stealth browser

**Device Integrity**
- [integrity-checker](https://github.com/luoshixin93-sudo/integrity-checker) - SafetyNet + Play Integrity + CTS checker
- [play-integrity-helper](https://github.com/luoshixin93-sudo/play-integrity-helper) - Play Integrity fix helper

**Cloud Infrastructure**
- [stealth-proxy-runner](https://github.com/luoshixin93-sudo/stealth-proxy-runner) - Headless stealth browser with Camoufox
- [docker-android-cloud-run](https://github.com/luoshixin93-sudo/docker-android-cloud-run) - Dockerized Android AVD
- [android-emulator-cloud](https://github.com/luoshixin93-sudo/android-emulator-cloud) - Docker emulator with noVNC
- [cloud-phone-gms-guide](https://github.com/luoshixin93-sudo/cloud-phone-gms-guide) - GMS installation guide

## Quick start

```bash
# Run IP checker (from any Android Cloud Device cloud device)
python ip_check.py

# Run device status checker
python device_status_checker.py

# Audit your entire fleet IP pool
python fleet_ip_audit.py
```

### Sample output - fleet_ip_audit.py

```
Android Cloud Device Fleet IP Audit
====================== [2026-07-14 10:00:00 UTC]
Scanning 5 devices...
Device-01 | 203.0.113.42 | HK    | Status: UNIQUE
Device-02 | 198.51.100.17 | US-CA | Status: UNIQUE
Device-03 | 203.0.113.42 | HK    | Status: !! DUPLICATE IP
Device-04 | 192.0.2.88    | SG    | Status: UNIQUE
Device-05 | 203.0.113.42 | HK    | Status: !! DUPLICATE IP
Fleet Size: 5 | Unique IPs: 3 | Duplicates: 2
Recommendation: Reroute Device-03 and Device-05 to different IP pools
```

## Use cases

| Use case | Why Android Cloud Device |
|----------|-------------|
| Social media marketing | Run many accounts, each on its own IP - no cross-linkage |
| Automation & bots | Scale scripts across isolated cloud Android instances |
| Multi-instance gaming | Parallel sessions without hardware or bans |
| App testing | Test across real devices and real geolocations |
| Fleet management | Monitor status of all cloud devices from one dashboard |

## File overview

| File | Description |
|------|-------------|
| ip_check.py | Public IP verification tool |
| device_status_checker.py | Cloud device health & status checker |
| fleet_ip_audit.py | Batch IP audit across device fleet |
| README.md | This file |

## Community Tools We Star

Android Cloud Device builds in the open. These are the tools in our stack:

- [playwright](https://github.com/microsoft/playwright) (92k stars) - Browser automation
- [scrcpy](https://github.com/Genymobile/scrcpy) (145k stars) - Android screen mirroring
- [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) (12k stars) - Stealth Chrome
- [camoufox](https://github.com/daijro/camoufox) (10k stars) - Anti-detection browser
- [fingerprintjs](https://github.com/fingerprintjs/fingerprintjs) (27k stars) - Browser fingerprinting
- [appium](https://github.com/appium/appium) (21k stars) - Mobile test automation

## Contact

| Channel | Address |
|---------|---------|
| Website | [android-cloud-device.com](https://www.android-cloud-device.com/) |
| WhatsApp | @along915 |
| Email | ailong9281@gmail.com |
| Telegram | [@Alongyun](https://t.me/Alongyun) |

---

*Star the repo if you find it useful. Issues and PRs welcome!*
