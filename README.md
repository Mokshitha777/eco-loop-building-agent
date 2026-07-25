# 🏢 Eco Loop Building AI

<img width="1919" height="774" alt="image" src="https://github.com/user-attachments/assets/cc37a41b-f373-4b4a-865d-66333c2a34b0" />
<img width="1901" height="693" alt="image" src="https://github.com/user-attachments/assets/b193c95e-6cb9-4621-bb2e-eea02069d036" />
<img width="1919" height="470" alt="image" src="https://github.com/user-attachments/assets/e1c65850-9b14-4a93-8c4a-2aa9a611cd4d" />

An AI-powered Smart Building Management System developed for the **Honeywell Smart Building Hackathon**.

The project combines **EnergyPlus**, **Python**, **Streamlit**, and a locally running **Gemma 3 Large Language Model (LLM)** through Ollama to monitor building conditions, analyse energy usage, and recommend energy-efficient actions.

---

# 📌 Overview

Buildings consume a significant amount of energy every day. Traditional Building Management Systems often rely on fixed rules and cannot intelligently adapt to changing conditions.

Eco Loop Building AI demonstrates how Artificial Intelligence can assist in analysing building data and recommending energy-saving actions while maintaining a comfortable indoor environment.

The project integrates building simulation, live sensor monitoring, AI-based analysis, and an interactive dashboard into a single application.

---

# 🚀 Features

- 🏢 EnergyPlus building simulation
- 📊 Live sensor monitoring
- 🤖 AI-powered building analysis using Gemma 3
- ⚡ Intelligent energy-saving recommendations
- 🌡 Temperature and humidity monitoring
- 👥 Occupancy detection
- 🌬 CO₂ level monitoring
- 🚨 Automatic building alerts
- 💚 Building Health Score
- 💬 AI Chat Assistant
- 🔄 Auto-refreshing dashboard

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend development |
| Streamlit | Dashboard |
| EnergyPlus | Building energy simulation |
| Ollama | Running local LLM |
| Gemma 3 (1B) | AI building analysis |
| Pandas | Data processing |

---

# 📂 Project Structure

```text
eco-loop-building-agent/

│
├── ai/
│   ├── agent.py
│   └── llm.py
│
├── dashboard/
│   └── app.py
│
├── energyplus/
│   ├── parser.py
│   ├── run_simulation.py
│   └── output/
│
├── simulator/
│   └── simulator.py
│
├── utils/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ How the Project Works

### Step 1 – Building Simulation

EnergyPlus simulates the building and generates energy consumption data.

↓

### Step 2 – Sensor Monitoring

The simulator provides live values for:

- Temperature
- Humidity
- Occupancy
- Energy Consumption
- CO₂ Level

↓

### Step 3 – AI Decision Engine

The AI agent analyses the sensor data and generates intelligent recommendations such as:

- Enable Energy Saving Mode
- Increase Ventilation
- Turn ON Air Conditioning
- Turn OFF Air Conditioning
- Turn OFF Lights when rooms are empty

↓

### Step 4 – AI Analysis

Gemma 3 analyses the building conditions and provides:

- Building health summary
- Energy efficiency observations
- Comfort analysis
- Energy-saving recommendations

↓

### Step 5 – Dashboard

The Streamlit dashboard displays all information in real time.

---

# 📊 Dashboard Includes

- Total Site Energy
- Baseline Energy
- Estimated Optimised Energy
- Estimated Energy Savings
- Live Sensor Data
- Building Alerts
- AI Control Decisions
- Building Health Score
- AI Building Analysis
- AI Chat Assistant

---

# 🤖 AI Features

The project uses **Gemma 3**, running locally through **Ollama**, to analyse building conditions.

The AI can:

- Analyse sensor readings
- Explain building status
- Recommend energy-saving actions
- Provide natural language responses
- Answer building-related questions

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Mokshitha777/eco-loop-building-agent.git
```

Move into the project

```bash
cd eco-loop-building-agent
```

Install the required packages

```bash
pip install -r requirements.txt
```

Make sure EnergyPlus and Ollama are installed on your system.

---

# ▶️ Running the Project

Run the main application

```bash
python main.py
```

Launch the dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📈 Future Improvements

Some possible future enhancements include:

- Integration with real IoT sensors
- Historical data storage
- Energy usage graphs
- Predictive energy forecasting
- Automatic EnergyPlus control updates
- Cloud deployment
- Mobile application support

---

# 👨‍💻 Team

Developed as part of the **Honeywell Smart Building AI Hackathon**.

---

# 📄 License

This project was developed for educational and hackathon purposes.
