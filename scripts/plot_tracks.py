import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "/Users/murathanakar/Aviation-Data-Project-1/data/processed/traffic_log.csv"
)

plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["tracks"], marker="o")

plt.title("Aircraft Tracks Over Time")
plt.xlabel("Time")
plt.ylabel("Tracks")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "/Users/murathanakar/Aviation-Data-Project-1/visualizations/tracks_over_time.png"
)

print("Tracks chart created")
