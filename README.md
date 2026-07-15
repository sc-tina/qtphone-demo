# 馃嚟馃嚢 QTPhone Demo 鈥?Global Independent IP Cloud Phone

> **Live Demo Repository** | [qtphone.com](https://www.qtphone.com/) | [Main Repo](https://github.com/luoshixin93-sudo/qtphone)

QTPhone provides **cloud Android devices with dedicated, independent IPs** 鈥?built for
social-media marketing, automation, gaming multi-instance, and large-scale app testing.

---

## 馃敡 What this repo shows

This repo demonstrates four QTPhone core capabilities:

| Script | What it does |
|--------|-------------|
| ip_check.py | Verify your cloud device's public IP address |
| device_status_checker.py | Real-time device health: screen, battery, network, apps, IP |
| leet_ip_audit.py | Batch IP verification across your entire device fleet |

## 馃啎 What's new (2026-07-14)

Four new open-source repos joined the QTPhone ecosystem today:

| Repo | Description |
|------|-------------|
| [integrity-checker](https://github.com/luoshixin93-sudo/integrity-checker) | Android device integrity audit CLI (SafetyNet + Play Integrity API + CTS profile) |
| [play-integrity-helper](https://github.com/luoshixin93-sudo/play-integrity-helper) | One-click Play Integrity fix helper for cloud Android devices |
| [cloud-phone-gms-guide](https://github.com/luoshixin93-sudo/cloud-phone-gms-guide) | Step-by-step GMS/Google Play Store installation on cloud phones |
| [appium-parallel-runner](https://github.com/luoshixin93-sudo/appium-parallel-runner) | Parallel Appium test runner for Android/iOS real devices |

## 馃殌 Full QTPhone Open-Source Ecosystem

15 open-source repos covering every layer of cloud Android infrastructure:

**Core Platform**
- [qtphone](https://github.com/luoshixin93-sudo/qtphone) 鈥?Main platform repo
- [cloudphone-sdk-python](https://github.com/luoshixin93-sudo/cloudphone-sdk-python) 鈥?Python SDK

**Testing & Automation**
- [appium-parallel-runner](https://github.com/luoshixin93-sudo/appium-parallel-runner) 鈥?Parallel Appium test runner
- [maestro-mobile-runner](https://github.com/luoshixin93-sudo/maestro-mobile-runner) 鈥?Fast Maestro UI test runner
- [stealth-browser-runner](https://github.com/luoshixin93-sudo/stealth-browser-runner) 鈥?Playwright stealth browser

**Device Integrity**
- [integrity-checker](https://github.com/luoshixin93-sudo/integrity-checker) 鈥?SafetyNet + Play Integrity + CTS checker
- [play-integrity-helper](https://github.com/luoshixin93-sudo/play-integrity-helper) 鈥?Play Integrity fix helper

**Cloud Infrastructure**
- [stealth-proxy-runner](https://github.com/luoshixin93-sudo/stealth-proxy-runner) 鈥?Headless stealth browser with Camoufox
- [docker-android-cloud-run](https://github.com/luoshixin93-sudo/docker-android-cloud-run) 鈥?Dockerized Android AVD
- [android-emulator-cloud](https://github.com/luoshixin93-sudo/android-emulator-cloud) 鈥?Docker emulator with noVNC
- [cloud-phone-gms-guide](https://github.com/luoshixin93-sudo/cloud-phone-gms-guide) 鈥?GMS installation guide

## 馃攲 Quick start

\\\ash
# Run IP checker (from any QTPhone cloud device)
python ip_check.py

# Run device status checker
python device_status_checker.py

# Audit your entire fleet IP pool
python fleet_ip_audit.py
\\\

### Sample output 鈥?fleet_ip_audit.py

\\\
QTPhone Fleet IP Audit
====================== [2026-07-14 10:00:00 UTC]
Scanning 5 devices...
Device-01 | 203.0.113.42 | HK | Status: 鉁?UNIQUE
Device-02 | 198.51.100.17 | US-CA | Status: 鉁?UNIQUE
Device-03 | 203.0.113.42 | HK | Status: 鈿狅笍 DUPLICATE IP
Device-04 | 192.0.2.88 | SG | Status: 鉁?UNIQUE
Device-05 | 203.0.113.42 | HK | Status: 鈿狅笍 DUPLICATE IP
Fleet Size: 5 | Unique IPs: 3 | Duplicates: 2
Recommendation: Reroute Device-03 and Device-05 to different IP pools
\\\

## 馃挕 Use cases

| Use case | Why QTPhone |
|----------|-------------|
| Social media marketing | Run many accounts, each on its own IP 鈥?no cross-linkage |
| Automation & bots | Scale scripts across isolated cloud Android instances |
| Multi-instance gaming | Parallel sessions without hardware or bans |
| App testing | Test across real devices and real geolocations |
| Fleet management | Monitor status of all cloud devices from one dashboard |

## 馃搨 File overview

| File | Description |
|------|-------------|
| ip_check.py | Public IP verification tool |
| device_status_checker.py | Cloud device health & status checker |
| leet_ip_audit.py | Batch IP audit across device fleet |
| README.md | This file |

## 馃敆 Community Tools We Star

QTPhone builds in the open. These are the tools in our stack:

- [playwright](https://github.com/microsoft/playwright) (92k 猸? 鈥?Browser automation
- [scrcpy](https://github.com/Genymobile/scrcpy) (145k 猸? 鈥?Android screen mirroring
- [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) (12k 猸? 鈥?Stealth Chrome
- [camoufox](https://github.com/daijro/camoufox) (10k 猸? 鈥?Anti-detection browser
- [fingerprintjs](https://github.com/fingerprintjs/fingerprintjs) (27k 猸? 鈥?Browser fingerprinting
- [appium](https://github.com/appium/appium) (21k 猸? 鈥?Mobile test automation

## 馃摓 Contact

| Channel | Address |
|---------|---------|
| 馃寪 Website | [qtphone.com](https://www.qtphone.com/) |
| 馃挰 WhatsApp | @along915 |
| 鉁夛笍 Email | ailong9281@gmail.com |
| 鉁堬笍 Telegram | [@Alongyun](https://t.me/Alongyun) |

---

*猸?Star the repo if you find it useful. Issues and PRs welcome!*