import json
import csv
import shutil
from datetime import datetime

# Canlı readsb çıktısı
json_file = "/Users/murathanakar/data/raw/aircraft.json"

# Dashboard'ın kullandığı JSON
dashboard_json = "/Users/murathanakar/Aviation-Data-Project-1/data/aircraft.json"

# CSV geçmiş dosyası
csv_file = "/Users/murathanakar/Aviation-Data-Project-1/data/history/aircraft_history.csv"

try:
    # Dashboard JSON'unu güncelle
    shutil.copy(json_file, dashboard_json)

    # Canlı JSON oku
    with open(json_file, "r") as f:
        data = json.load(f)

except Exception as e:
    print("JSON okunamadı:", e)
    raise SystemExit(1)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)

    for ac in data.get("aircraft", []):

        flight = (ac.get("flight") or "").strip()

        lat = ac.get("lat")
        lon = ac.get("lon")

        if lat is None:
            lat = ac.get("lastPosition", {}).get("lat")

        if lon is None:
            lon = ac.get("lastPosition", {}).get("lon")

        if not flight:
            continue

        if lat is None or lon is None:
            continue

        writer.writerow([
            timestamp,
            flight,
            lat,
            lon,
            ac.get("track"),
            ac.get("gs"),
            ac.get("alt_baro"),
            ac.get("rssi")
        ])
