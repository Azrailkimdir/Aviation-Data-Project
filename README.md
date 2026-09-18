# Aviation Data Project

Aviation Data Project is an ongoing aerospace and aviation data initiative that explores real-world aircraft operations through ADS-B technology, OpenSky Network integration, flight tracking, and data analysis.

The project combines aviation, programming, software-defined radio (SDR), hardware systems, and data analytics to collect, visualize, and analyze real aircraft traffic data using a personal ADS-B receiving station.

---

## Project Vision

This project began with a simple question:

**What can real-world aircraft data teach us about aviation operations?**

By building and operating a personal ADS-B ground station, I aim to better understand aircraft systems, air traffic activity, flight behavior, and aviation data analytics while developing skills in programming, data analysis, and engineering problem-solving.

---

# Phase 1 – ADS-B Ground Station ✅

The first phase focused on building a working ADS-B data collection system capable of receiving, decoding, storing, and visualizing aircraft telemetry.

---

## ADS-B Ground Station Setup

The image below shows the operational ADS-B receiving station used for this project.

The setup includes an RTL-SDR Blog V3 receiver, dipole antenna system, and a laptop running ADS-B decoding and data collection services.

![ADS-B Ground Station](ground-station-setup.jpg)

*Operational ADS-B receiving station used for real-time aircraft tracking, OpenSky Network integration, and aviation data collection.*

### Ground Station Components

- RTL-SDR Blog V3 Receiver
- ADS-B Dipole Antenna
- readsb Decoder
- OpenSky Network Feeder
- Real-Time Data Collection Services
- Aviation Analytics Infrastructure

---

## Hardware & Software

### Hardware

- RTL-SDR Blog V3
- ADS-B Antenna System
- Personal ADS-B Ground Station

### Software

- readsb
- OpenSky Network Feeder
- Python
- JSON Data Streams
- CSV Logging System
- Web-Based Radar Dashboard
- Docker

---

## System Deployment

### OpenSky Network Account

The ADS-B ground station is connected to the OpenSky Network and contributes aircraft tracking data to the global aviation research community.

![OpenSky Account](opensky-account.png)

*OpenSky Network account used for ADS-B data contribution.*

---

### OpenSky Sensor Registration

The ADS-B receiver has been successfully registered and approved as an OpenSky data source.

![OpenSky Sensors](opensky-sensors.png)

*Registered and approved ADS-B sensors within the OpenSky Network.*

---

### ADS-B Infrastructure

The system operates through a Docker-based deployment environment supporting ADS-B decoding, data collection, OpenSky integration, and dashboard services.

![Docker Services](docker-services.png)

*Docker containers supporting ADS-B data collection and OpenSky feeder operations.*

---

## Sarp's ADS-B Radar Map

A custom web-based radar dashboard developed to visualize real-time ADS-B aircraft telemetry collected by the personal ground station.

The dashboard provides a live view of aircraft positions, tracks, and telemetry data while supporting ongoing aviation data collection and analysis.

![Radar Dashboard](radar-dashboard.png)

*Real-time aircraft tracking dashboard connected to the ADS-B ground station.*

### Dashboard Features

✅ Real-time aircraft tracking

✅ Live ADS-B telemetry visualization

✅ Position and track monitoring

✅ Aircraft movement observation

✅ Integration with JSON data streams

✅ Support for future aviation analytics

---

## System Architecture

```text
RTL-SDR Blog V3
        │
        ▼
      readsb
        │
        ├── JSON Feed
        ├── CSV Logging
        ├── Radar Dashboard
        └── OpenSky Network
```

---

## Data Sources

- RTL-SDR Receiver
- ADS-B Broadcast Messages
- readsb Decoder
- OpenSky Network
- Real-Time Aircraft Telemetry

---

## Current Status

✅ Real-time aircraft tracking

✅ Aircraft position decoding

✅ Historical ADS-B data collection

✅ Automated CSV logging

✅ Live JSON telemetry feed

✅ Raw ADS-B hexadecimal message capture

✅ ADS-B protocol level data collection

✅ Telemetry decoding validation

✅ OpenSky Network data contribution

✅ Interactive radar dashboard

✅ Aircraft traffic monitoring

✅ Historical aircraft telemetry archiving

✅ Data collection for future analytics

---

## Current Capabilities

✅ Real-time aircraft tracking

✅ Aircraft position decoding

✅ Historical ADS-B data collection

✅ Automated CSV logging

✅ Live JSON telemetry feed

✅ OpenSky Network integration

✅ Interactive radar dashboard

✅ Aircraft traffic monitoring

✅ Data collection for future analytics

---

## Initial Results

✅ Personal ADS-B ground station successfully deployed

✅ Real-time aircraft tracking operational

✅ Continuous ADS-B telemetry collection established

✅ Automated historical data logging active

✅ Aircraft position and track decoding verified

✅ OpenSky Network feeder operational

✅ Aviation analytics infrastructure established

✅ Real-world aircraft data available for future research and visualization projects

---

# Phase 2 – Aircraft Traffic Analysis Around Ankara 🚧

The second phase of the project focuses on transforming collected aircraft telemetry into meaningful aviation insights.

### Planned Areas of Analysis

- Aircraft Traffic Analysis Around Ankara
- Aircraft Type Distribution Analysis
- Flight Altitude Analysis
- Aircraft Activity by Time of Day
- Traffic Density Visualization
- Aircraft Route Analysis
- Python-Based Aviation Analytics
- ADS-B Data Visualization Dashboards
- OpenSky Network Contribution Metrics

---

# Why This Project Matters

This project goes beyond simple aircraft tracking.

It combines radio-frequency technology, software-defined radio, aviation systems, programming, visualization, and real-world data collection into a single engineering-focused learning experience.

By collecting ADS-B telemetry and contributing data to the OpenSky Network, the project provides hands-on exposure to technologies used in modern aviation, air traffic monitoring, and aerospace-related data systems.

---

# Educational Value

This project combines:

- Aviation
- Aerospace Learning
- Programming
- Data Analysis
- Radio Frequency Technology
- Software Defined Radio (SDR)
- Open Data Contribution
- Citizen Science
- Engineering Problem Solving

while providing hands-on experience with real-world aircraft data and modern flight-tracking technologies.

---

# Repository Structure

```text
data/
├── raw/
├── processed/
└── archive/

scripts/

dashboard/

visualizations/

docs/

images/
├── ground-station-setup.jpg
├── opensky-account.png
├── opensky-sensors.png
├── docker-services.png
└── radar-dashboard.png
```

---

# Future Development

Planned future improvements include:

- Advanced aircraft traffic analytics
- Historical trend analysis
- Aircraft type recognition tools
- Interactive data visualizations
- Automated reporting systems
- Real-time flight statistics
- Python-based analytics dashboards
- Expanded OpenSky Network integration

---

# Author

## Sarp Akar

Sept 2026

Always Curious. Always Learning.
