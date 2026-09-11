import json

with open("../data/raw/stats.json", "r") as f:
    data = json.load(f)

total = data["total"]

print("=== Aviation Data Report ===")
print()

print("Valid Messages:", total["messages_valid"])
print("Aircraft Tracks:", total["tracks"]["all"])
print("Decoded Positions:", total["position_count_total"])
print("Signal Level:", total["local"]["signal"], "dB")
print("Noise Level:", total["local"]["noise"], "dB")
