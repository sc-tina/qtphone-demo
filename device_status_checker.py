#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Android Cloud Device Device Status Checker (demo feature)
=============================================
Reports real-time status of a cloud Android device:
  - Firmware & CPU info
  - Screen state & resolution
  - Battery level & charging status
  - Network connection & SSID
  - Public IP (independent per Android Cloud Device device)
  - Top installed apps (social media focus)

Intended for cloud device fleet operators who need to
monitor hundreds of Android Cloud Device instances programmatically.

Usage:
    python device_status_checker.py

Requires: Python 3.7+. No third-party dependencies.
On a real Android Cloud Device device this can be enhanced with ADB
calls to retrieve device-specific data.

Note: This demo uses simulated/system info as a standalone script.
Replace the _get_* stubs with real ADB calls when running
inside a Android Cloud Device cloud environment.
"""
import json
import socket
import urllib.request
import platform

# ── simulated device data ──────────────────────────────────────────
# In production, replace these with real ADB calls to your cloud device.
# Example ADB-equivalent calls (require db CLI + USB/network):
#   adb shell getprop ro.build.version.release
#   adb shell dumpsys battery | grep level
#   adb shell wm size
#   adb shell dumpsys connectivity | grep SSID

ANDROID_VERSION = "14"
CPU_ARCH = "arm64-v8a"
DEVICE_MODEL = "Android Cloud Device-Cloud-G1"
SCREEN_ON = True
SCREEN_RES = "1080x2400"
REFRESH_RATE = "60Hz"
BATTERY_PCT = 85
BATTERY_CHARGING = True
NETWORK_TYPE = "WiFi"
SSID = "Android Cloud Device-Cloud"
SOCIAL_APPS = [
    ("com.whatsapp", "WhatsApp"),
    ("org.telegram.messenger", "Telegram"),
    ("com.twitter.android", "Twitter/X"),
    ("com.instagram.android", "Instagram"),
    ("com.snapchat.android", "Snapchat"),
    ("com.facebook.katana", "Facebook"),
    ("com.zhiliaoapp.musically", "TikTok"),
    ("com.google.android.youtube", "YouTube"),
    ("jp.naver.lineandroid", "LINE"),
    ("com.vkontakte.android", "VK"),
]

# ── helpers ──────────────────────────────────────────────────────────

def get_public_ip():
    """Fetch the public IP this device presents to the internet."""
    try:
        req = urllib.request.Request(
            "https://ipapi.co/json/",
            headers={"User-Agent": "Android Cloud Device-DeviceChecker/1.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data.get("ip", "unavailable"), data.get("country_name", "unknown")
    except Exception as e:
        return "unavailable", str(e)


def check_port_open(host: str, port: int, timeout: float = 2.0) -> bool:
    """Check if a port is reachable (useful for ADB-over-IP health checks)."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        sock.close()
        return True
    except Exception:
        return False


def render_status():
    ip, country = get_public_ip()
    verdict = "✅ All systems operational"
    if not SCREEN_ON:
        verdict = "⚠️  Screen is OFF — device may be idle"
    if ip == "unavailable":
        verdict = "❌ Cannot reach public IP service"

    divider = "-" * 30
    print("Android Cloud Device Device Status Checker")
    print("=" * 30)
    print(f"Device    : {DEVICE_MODEL}")
    print(divider)
    print(f"Firmware  : Android {ANDROID_VERSION}")
    print(f"CPU Arch  : {CPU_ARCH}")
    print(divider)
    print(f"Screen    : {'ON' if SCREEN_ON else 'OFF'} ({SCREEN_RES} @ {REFRESH_RATE})")
    print(f"Battery   : {BATTERY_PCT}% | Charging: {'Yes' if BATTERY_CHARGING else 'No'}")
    print(f"Network   : {NETWORK_TYPE} | SSID: {SSID}")
    print(f"IP        : {ip} ({country})")
    print(divider)
    print("Installed social apps (top 10):")
    for pkg, name in SOCIAL_APPS[:10]:
        print(f"  {pkg}  - {name}")
    print(divider)
    print(f"Verdict  : {verdict}")

    # ADB-over-IP health check (example host:port)
    adb_host = "10.0.0.100"   # Replace with your Android Cloud Device device IP
    adb_port = 5555
    adb_reachable = check_port_open(adb_host, adb_port)
    print(f"ADB ({adb_host}:{adb_port}): {'✅ Reachable' if adb_reachable else '⚠️  Not reachable'}")

    print()
    print("To run ADB commands against your Android Cloud Device device:")
    print(f"  1. Connect:  adb connect {adb_host}:{adb_port}")
    print(f"  2. Check:    adb -s {adb_host}:{adb_port} shell getprop")
    print(f"  3. Install:   adb -s {adb_host}:{adb_port} install your_app.apk")


if __name__ == "__main__":
    render_status()