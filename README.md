# Eco Loop Building AI

## Overview

Eco Loop Building AI is a smart building energy management system developed for the Honeywell Hackathon.

The project combines EnergyPlus building simulation with a locally running Large Language Model (Gemma 3 using Ollama) to monitor building conditions, analyse sensor data, and recommend energy-saving actions in real time.

The dashboard refreshes automatically every few seconds and displays live sensor values, AI decisions, building health, and EnergyPlus simulation results.

---

## Features

- EnergyPlus building simulation
- Live building sensor monitoring
- AI-based building analysis using Gemma 3
- Rule-based control decisions
- Building health score
- Energy saving estimation
- Automatic dashboard refresh
- Interactive AI assistant for building-related questions

---

## Technologies Used

- Python
- Streamlit
- EnergyPlus
- Ollama
- Gemma 3 (1B)
- Pandas

---

## Project Structure

```
eco-loop-building-agent/

├── ai/
│   ├── agent.py
│   └── llm.py

├── dashboard/
│   └── app.py

├── energyplus/
│   ├── parser.py
│   ├── output/
│   └── simulation files

├── simulator/
│   └── simulator.py

├── utils/

├── main.py
├── requirements.txt
└── README.md
```

---

## How It Works

1. EnergyPlus simulates the building.
2. Sensor values are generated for temperature, humidity, occupancy, energy usage and CO₂.
3. The AI agent analyses these values.
4. Control decisions such as increasing ventilation or enabling energy-saving mode are generated.
5. The dashboard displays the simulation results, alerts, AI decisions and overall building health.

---

## AI Decisions

The AI recommends actions such as:

- Enable Energy Saving Mode
- Increase Ventilation
- Turn ON Air Conditioning
- Turn OFF Air Conditioning
- Turn OFF Lights (when no occupancy)

These decisions are generated automatically based on the current building conditions.

---

## Dashboard

The Streamlit dashboard includes:

- EnergyPlus simulation results
- Live sensor data
- Building alerts
- AI control decisions
- Building health score
- AI analysis
- Chat interface to ask building-related questions

---

## Future Improvements

- Real-time IoT sensor integration
- Historical data storage and trend analysis
- Automatic control updates to EnergyPlus
- Predictive energy forecasting
- Cloud deployment

---

## Team

Developed for the Honeywell Smart Building AI Hackathon.
