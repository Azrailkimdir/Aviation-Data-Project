import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/history/aircraft_history_v2.csv"
)

df["timestamp"] = pd.to_datetime(df["timestamp"])

df["hour"] = df["timestamp"].dt.hour

hourly_unique = (
    df.groupby("hour")["hex"]
      .nunique()
)

print(hourly_unique)

plt.figure(figsize=(10,5))

hourly_unique.plot(kind="bar")

plt.title(
    "Unique Aircraft by Hour"
)

plt.xlabel("Hour of Day")
plt.ylabel("Unique Aircraft")

plt.tight_layout()

plt.savefig(
    "visualizations/unique_aircraft_by_hour.png",
    dpi=300
)

print("Graph saved.")
