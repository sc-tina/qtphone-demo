#!/usr/bin/env python3
"""QTPhone Fleet IP Audit 鈥?Batch IP verification across your device fleet."""
import json, sys, urllib.request, time
from datetime import datetime

API_BASE = "https://api.qtphone.com/v1"  # Replace with real endpoint

def get_public_ip():
    try:
        r = urllib.request.urlopen("https://api.ipify.org?format=json", timeout=10)
        return json.loads(r.read())["ip"]
    except Exception as e:
        return f"ERROR: {e}"

def get_device_ip(device_id, api_key=None):
    headers = {"User-Agent": "QTPhone-FleetAudit/1.0"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    try:
        req = urllib.request.Request(f"{API_BASE}/devices/{device_id}/status", headers=headers)
        resp = urllib.request.urlopen(req, timeout=10)
        data = json.loads(resp.read())
        return data.get("ip", "UNKNOWN"), data.get("country", "N/A")
    except Exception:
        return get_public_ip(), "N/A"

def audit_fleet(path=None, api_key=None):
    print("QTPhone Fleet IP Audit")
    print("=" * 50)
    print(f"[{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC]")
    if path:
        with open(path) as f:
            devices = json.load(f)
    else:
        devices = [
            {"id": "demo-01", "name": "Device-01"},
            {"id": "demo-02", "name": "Device-02"},
            {"id": "demo-03", "name": "Device-03"},
            {"id": "demo-04", "name": "Device-04"},
            {"id": "demo-05", "name": "Device-05"},
        ]
    print(f"Scanning {len(devices)} devices...\n")
    results = []
    for d in devices:
        ip, country = get_device_ip(d["id"], api_key)
        results.append({"name": d["name"], "ip": ip, "country": country})
        print(f"{d['name']} | {ip} | {country}")
        time.sleep(0.3)
    print("\n" + "=" * 50)
    ip_count = {}
    for r in results:
        ip_count[r["ip"]] = ip_count.get(r["ip"], 0) + 1
    duplicates = {ip: cnt for ip, cnt in ip_count.items() if cnt > 1 and not ip.startswith("ERROR")}
    print(f"Fleet Size: {len(devices)} | Unique IPs: {len(ip_count)-len(duplicates)} | Duplicates: {len(duplicates)}")
    if duplicates:
        print("\nDuplicate IPs detected:")
        for ip, cnt in duplicates.items():
            dupes = [r["name"] for r in results if r["ip"] == ip]
            print(f"  {ip} ({cnt}x): {', '.join(dupes)}")
    else:
        print("\nAll devices have unique IPs!")
    return results

if __name__ == "__main__":
    audit_fleet(sys.argv[1] if len(sys.argv) > 1 else None)