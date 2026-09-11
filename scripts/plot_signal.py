import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "/Users/murathanakar/Aviation-Data-Project-1/data/processed/traffic_log.csv"
)

plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["signal"], marker="o")

plt.title("Signal Strength Over Time")
plt.xlabel("Time")
plt.ylabel("Signal (dB)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "/Users/murathanakar/Aviation-Data-Project-1/visualizations/signal_strength.png"
)

print("Signal chart created")
