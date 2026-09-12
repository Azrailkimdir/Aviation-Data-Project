import json
import csv
from datetime import datetime

json_file = "/Users/murathanakar/tar1090/html/data/aircraft.json"
csv_file = "/Users/murathanakar/Aviation-Data-Project-1/data/history/aircraft_history.csv"

with open(json_file, "r") as f:
    data = json.load(f)

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
