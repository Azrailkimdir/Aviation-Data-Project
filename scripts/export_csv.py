import json
import csv
import os
from datetime import datetime

with open("../data/raw/stats.json", "r") as f:
    data = json.load(f)

total = data["total"]

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

row = [
    timestamp,
    total["messages_valid"],
    total["tracks"]["all"],
    total["position_count_total"],
    total["local"]["signal"],
    total["local"]["noise"]
]

csv_file = "../data/processed/traffic_log.csv"

file_exists = os.path.isfile(csv_file)

with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow([
            "timestamp",
            "messages",
            "tracks",
            "positions",
            "signal",
            "noise"
        ])

    writer.writerow(row)

print("Data exported to traffic_log.csv")
