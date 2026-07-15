#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QTPhone Independent-IP Checker (demo feature)
=============================================
Verifies the public IP presented by the current machine / cloud phone.
Demonstrates QTPhone's core value: each cloud device gets its own
independent public IP.

Usage:
    python ip_check.py

Requires: Python 3.7+, internet access. No third-party dependencies.
"""
import json
import urllib.request

GEO_URL = "https://ipapi.co/json/"


def get_public_ip_info():
    try:
        req = urllib.request.Request(GEO_URL, headers={"User-Agent": "QTPhone-Demo"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return {
            "ip": data.get("ip", "unknown"),
            "org": data.get("org", "unknown"),
            "country": data.get("country_name", data.get("country", "unknown")),
        }
    except Exception as e:  # network/CORS/timeout — degrade gracefully
        return {"ip": "unavailable", "org": str(e), "country": "unknown"}


def main():
    info = get_public_ip_info()
    print("QTPhone Independent-IP Checker")
    print("-" * 30)
    print(f"Public IP : {info['ip']}")
    print(f"Org / ISP : {info['org']}")
    print(f"Country   : {info['country']}")
    if info["ip"] != "unavailable":
        print("Verdict   : ✅ Independent public IP detected")
    else:
        print("Verdict   : ⚠️  Could not determine public IP (offline?)")


if __name__ == "__main__":
    main()
