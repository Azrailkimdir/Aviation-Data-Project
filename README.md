# Aviation Data Project #1

Aviation Data Project #1 explores real-world aircraft operations through ADS-B technology, OpenSky Network integration, flight tracking, and data analysis.

The project combines aviation, programming, hardware, and data analytics to collect, visualize, and analyze real aircraft traffic data using a personal ADS-B receiving station.

---

## Project Objective

The purpose of this project is to collect and analyze real-world aviation data using ADS-B technology while learning more about aircraft operations, flight tracking systems, aviation analytics, and air traffic patterns.

The project also serves as a hands-on introduction to radio frequency technology, software-defined radio (SDR), data collection, and Python-based aviation analytics.

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

docs/images/opensky-account.png

*OpenSky Network account used for ADS-B data contribution.*

---

### OpenSky Sensor Registration

The ADS-B receiver has been successfully registered and approved as an OpenSky data source.

docs/images/opensky-sensors.png

*Registered and approved ADS-B sensors within the OpenSky Network.*

---

### ADS-B Infrastructure

The system operates through a Docker-based deployment environment supporting ADS-B decoding, data collection, OpenSky integration, and dashboard services.

docs/images/docker-services.png

*Docker containers supporting ADS-B data collection and OpenSky feeder operations.*

---

## System Architecture

RTL-SDR Blog V3
        │
        ▼
      readsb
        │
        ├── JSON Feed
        ├── CSV Logging
        ├── Radar Dashboard
        └── OpenSky Network

---

## Data Sources

- RTL-SDR Receiver
- ADS-B Broadcast Messages
- readsb Decoder
- OpenSky Network
- Real-Time Aircraft Telemetry

---

## Current Status

✅ RTL-SDR configured

✅ ADS-B messages received

✅ Aircraft positions decoded

✅ JSON data collection active

✅ Historical CSV logging active

✅ Automated startup configured

✅ OpenSky Network feeder online

✅ Real-time radar dashboard operational

✅ Docker deployment operational

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

- 193 valid ADS-B messages captured
- 53 aircraft tracks observed
- 5 aircraft positions successfully decoded
- Continuous ADS-B monitoring established
- OpenSky Network data contribution active

---

## Research Goals

The long-term goal of this project is to transform raw ADS-B messages into meaningful aviation insights through data analysis, visualization, and engineering-focused research.

Planned areas of exploration include:

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

## Educational Value

This project combines multiple disciplines:

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

## Repository Structure

data/
├── raw/
├── processed/
└── archive/

scripts/

dashboard/

visualizations/

docs/
└── images/
    ├── opensky-account.png
    ├── opensky-sensors.png
    └── docker-services.png

---

## Future Development

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

## Author

Sarp Akar
