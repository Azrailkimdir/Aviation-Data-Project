import pandas as pd
import matplotlib.pyplot as plt

# Load ADS-B data
df = pd.read_csv(
    "data/history/aircraft_history_v2.csv"
)

# Keep only records with coordinates
df = df.dropna(
    subset=["lat", "lon"]
)

print(f"Coordinate observations: {len(df):,}")

# Flight corridor density map
plt.figure(figsize=(12, 8))

hb = plt.hexbin(
    df["lon"],
    df["lat"],
    gridsize=50,
    cmap="viridis",
    mincnt=1
)

plt.colorbar(
    hb,
    label="Route Density"
)

plt.title(
    "Flight Corridor Density Around Ankara"
)

plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.tight_layout()

plt.savefig(
    "visualizations/flight_corridors_ankara.png",
    dpi=300
)

print("Flight corridor map saved.")
