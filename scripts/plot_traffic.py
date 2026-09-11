import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/processed/traffic_log.csv")

plt.figure(figsize=(10,5))
plt.plot(df["timestamp"], df["messages"], marker="o")

plt.title("ADS-B Messages Over Time")
plt.xlabel("Time")
plt.ylabel("Valid Messages")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("../visualizations/traffic_over_time.png")

print("Chart created")
