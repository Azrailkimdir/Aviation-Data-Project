import pandas as pd
import matplotlib.pyplot as plt

csv_file = "data/history/aircraft_history_v2.csv"

df = pd.read_csv(csv_file)

df["timestamp"] = pd.to_datetime(df["timestamp"])

df["hour"] = df["timestamp"].dt.hour

hourly = df.groupby("hour").size()

print(hourly)

plt.figure(figsize=(10, 5))
hourly.plot(kind="bar")

plt.title("Aircraft Activity by Time of Day")
plt.xlabel("Hour of Day")
plt.ylabel("Aircraft Observations")

plt.tight_layout()

plt.savefig(
    "visualizations/aircraft_activity_by_hour.png",
    dpi=300
)

print("Graph saved.")
