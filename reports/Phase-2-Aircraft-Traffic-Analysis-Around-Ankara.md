# Phase 2 – Aircraft Traffic Analysis Around Ankara

Part of Aviation Data Project

This phase focuses on transforming real ADS-B aircraft telemetry into meaningful aviation insights through analysis, visualization, and research.

## Project Goal

I wanted to understand what aircraft traffic around Ankara looks like using real ADS-B data collected through my personal ground station.

This phase of the Aviation Data Project focuses on transforming raw aircraft telemetry into meaningful aviation insights through data collection, visualization, and analysis.

---

## Research Questions

- When is aircraft activity around Ankara at its highest?
- Which aircraft types appear most frequently?
- What altitude ranges are most commonly observed?
- What flight corridors are most commonly used?
- What patterns can be identified from locally collected ADS-B data?

---

## Data Source

Data collected through:

- RTL-SDR Blog V3
- ADS-B Ground Station
- readsb
- OpenSky Network Integration

---

## Planned Analysis

### Aircraft Activity by Time of Day

- Morning traffic
- Afternoon traffic
- Evening traffic
- Night traffic

### Aircraft Type Distribution

- Most common aircraft models
- Airline distribution
- Fleet composition

### Flight Altitude Analysis

- Average altitude
- Arrival vs departure profiles
- Overflight patterns

### Flight Corridor Analysis

- Common arrival routes
- Common departure routes
- Aircraft movement patterns around Ankara

---

## Current Status

✅ ADS-B ground station operational

✅ OpenSky Network contribution active

✅ Continuous ADS-B data collection established

✅ Historical CSV logging active

✅ JSON telemetry collection active

✅ Radar dashboard operational

✅ Over 7 days of aircraft telemetry collected

✅ Initial data analysis phase started

---

## Notes

This project builds upon the ADS-B infrastructure established during Phase 1 of the Aviation Data Project.

## First Analysis

### Aircraft Activity by Time of Day

Status:

✅ Data collection completed

✅ Preliminary dataset available

🚧 Analysis in progress

---

Objective:

To identify the periods of highest and lowest aircraft activity around Ankara using ADS-B telemetry data collected through the ground station.

Variables:

- Timestamp
- Aircraft Count
- Hour of Day

Expected Outcome:

A visualization showing how aircraft activity changes throughout the day and identifying peak traffic periods.

---

# Analysis #1 Completed

## Aircraft Activity by Time of Day

### Dataset

- 1,705 ADS-B observations
- Data collected using a local RTL-SDR ADS-B ground station
- Collection period: approximately 1.5–2 weeks
- Source: readsb + OpenSky integrated receiver

### Methodology

Two analytical approaches were applied:

#### 1. Total Aircraft Observations

All recorded ADS-B observations were grouped by local hour.

#### 2. Unique Aircraft Analysis

Aircraft were identified by their HEX addresses.

Multiple observations of the same aircraft within a time period were treated as a single aircraft presence.

### Visualization

#### Total Aircraft Observations by Hour

../visualizations/aircraft_activity_by_hour.png

### Results

| Hour | Unique Aircraft Observed |
|------|--------------------------|
| 08 | 6 |
| 09 | 6 |
| 11 | 6 |
| 12 | 14 |
| 13 | 18 |
| 14 | 1 |
| 17 | 8 |
| 18 | 96 |
| 19 | 73 |
| 20 | 38 |
| 21 | 20 |

### Key Findings

- Aircraft activity reached its highest level during the 18:00 hour.
- A total of 96 unique aircraft were observed during the busiest observed period.
- Traffic remained high between 18:00 and 20:00.
- Evening activity was significantly higher than activity observed during other periods.

### Discussion

Analysis of 1,705 ADS-B observations indicates a clear concentration of aircraft activity during evening hours around Ankara.

Both raw observation counts and unique HEX-based aircraft counts point to the same trend, suggesting that the observed evening peak is not simply caused by repeated recordings of the same aircraft.

As additional telemetry is collected, future analyses will determine whether this pattern remains consistent over longer observation periods.

### Status

✅ Completed


