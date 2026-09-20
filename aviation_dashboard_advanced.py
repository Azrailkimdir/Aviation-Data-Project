import pandas as pd
import matplotlib.pyplot as plt

# Veri yükleme
df = pd.read_csv("data/history/aircraft_history_v2.csv")

# Dönüşümler
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour

df["operator"] = (
    df["callsign"]
    .astype(str)
    .str.extract(r"([A-Z]+)")
)

df["altitude"] = pd.to_numeric(
    df["altitude"],
    errors="coerce"
)

# Dashboard
fig, axs = plt.subplots(
    2,
    2,
    figsize=(15, 10)
)

# --------------------------------------------------
# Top Operators
# --------------------------------------------------

top_ops = df["operator"].value_counts().head(5)

axs[0, 0].bar(
    top_ops.index,
    top_ops.values,
)

axs[0, 0].set_title(
    "Top 5 Operators"
)

axs[0, 0].set_ylabel(
    "Observations"
)

# --------------------------------------------------
# Activity by Hour
# --------------------------------------------------

hourly = (
    df["hour"]
    .value_counts()
    .sort_index()
)

axs[0, 1].plot(
    hourly.index,
    hourly.values,
    marker="o"
)

axs[0, 1].set_title(
    "Activity by Hour"
)

axs[0, 1].set_xlabel(
    "Hour"
)

axs[0, 1].set_ylabel(
    "Observations"
)

# --------------------------------------------------
# Altitude Distribution
# --------------------------------------------------

axs[1, 0].hist(
    df["altitude"].dropna(),
    bins=20
)

axs[1, 0].set_title(
    "Altitude Distribution"
)

axs[1, 0].set_xlabel(
    "Altitude (ft)"
)

axs[1, 0].set_ylabel(
    "Observations"
)

# --------------------------------------------------
# KPI Summary
# --------------------------------------------------

axs[1, 1].axis("off")

summary = (
    f"Total Observations : {len(df):,}\n\n"
    f"Unique Aircraft : {df['hex'].nunique()}\n\n"
    f"Unique Operators : {df['operator'].nunique()}\n\n"
    f"Average Altitude : {df['altitude'].mean():.0f} ft\n\n"
    f"Highest Altitude : {df['altitude'].max():.0f} ft\n\n"
    f"Most Active Hour : "
    f"{df['hour'].value_counts().idxmax():02d}:00\n\n"
    f"Latest Observation :\n"
    f"{df['timestamp'].max()}"
)

axs[1, 1].text(
    0.02,
    0.5,
    summary,
    fontsize=12,
    va="center"
)

# --------------------------------------------------

plt.suptitle(
    "Aviation Analytics Dashboard",
    fontsize=18
)

plt.tight_layout()

plt.savefig(
    "visualizations/aviation_dashboard_advanced.png",
    dpi=300
)

print("Advanced dashboard saved.")
