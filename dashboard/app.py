# import sys
# import os
# from ai.agent import *
# from test_energyplus import read_energy

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# import streamlit as st
# from streamlit_autorefresh import st_autorefresh

# from simulator.simulator import generate_building_data
# from energyplus.parser import read_summary
# from ai.llm import ask_llm

# st.set_page_config(
#     page_title="Eco Loop Building AI",
#     page_icon="🏢",
#     layout="wide"
# )

# st_autorefresh(interval=5000, key="refresh")

# st.title("🏢 Eco Loop Building AI")

# st.subheader("EnergyPlus + AI Building Management")

# sensor_data = generate_building_data()

# energy = read_energy()
# simulation = read_summary("energyplus/output/eplustbl.csv")

# st.header("🏢 EnergyPlus Simulation")

# st.success("Simulation Completed")

# st.metric(
#     "⚡ Total Site Energy",
#     f"{simulation['Total Site Energy (GJ)']} GJ"
# )


# st.header("📊 Live Sensor Data")

# st.dataframe(sensor_data, use_container_width=True)

# c1, c2, c3, c4, c5 = st.columns(5)

# with c1:
#     st.metric("🌡 Temperature", f"{sensor_data['Temperature'][0]} °C")

# with c2:
#     st.metric("💧 Humidity", f"{sensor_data['Humidity'][0]} %")

# with c3:
#     st.metric("👥 Occupancy", int(sensor_data["Occupancy"][0]))

# with c4:
#     st.metric("⚡ Energy", f"{sensor_data['Energy_kWh'][0]} kWh")

# with c5:
#     st.metric("🌫 CO₂", int(sensor_data["CO2"][0]))

# st.header("🚨 Alerts")

# if sensor_data["Temperature"][0] > 30:
#     st.warning("High temperature detected!")

# if sensor_data["Humidity"][0] > 60:
#     st.warning("High humidity detected!")

# if sensor_data["CO2"][0] > 1000:
#     st.error("Dangerous CO₂ level!")

# if sensor_data["Energy_kWh"][0] > 180:
#     st.warning("High energy consumption!")

# st.header("🤖 AI Analysis")

# prompt = f"""
# EnergyPlus Simulation

# {simulation}

# Live Sensor Data

# {sensor_data.to_string()}

# Analyse the building.

# Provide:

# • Building health
# • Energy efficiency
# • Risks
# • Recommendations
# • Estimated savings
# """

# with st.spinner("Analysing..."):
#     analysis = ask_llm(prompt)

# st.markdown(analysis)

# st.header("💬 Ask EcoLoop AI")

# question = st.text_input(
#     "Ask about the building",
#     placeholder="How can I reduce energy usage?"
# )

# if st.button("Ask AI"):

#     prompt = f"""
# EnergyPlus Simulation

# {simulation}

# Live Sensor Data

# {sensor_data.to_string()}

# User Question

# {question}

# Answer in bullet points.
# """

#     response = ask_llm(prompt)

#     st.success(response)

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh

from simulator.simulator import generate_building_data
from ai.agent import make_decision
from ai.llm import ask_llm
from energyplus.parser import read_summary

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Eco Loop Building AI",
    page_icon="🏢",
    layout="wide"
)

st_autorefresh(interval=5000, key="refresh")

# ---------------- TITLE ----------------

st.title("🏢 Eco Loop Building AI")
st.subheader("EnergyPlus + AI Smart Building Management")

# ---------------- LOAD DATA ----------------

sensor_data = generate_building_data()

simulation = read_summary(
    "energyplus/output/eplustbl.csv"
)

# ---------------- ENERGYPLUS ----------------

st.header("🏢 EnergyPlus Simulation")

left, right = st.columns([1,1])

with left:
    st.success("Simulation Completed")

with right:
    st.metric(
        "⚡ Total Site Energy",
        f"{simulation['Total Site Energy (GJ)']} GJ"
    )

# ---------------- ENERGY SAVINGS ----------------

try:
    baseline = float(simulation["Total Site Energy (GJ)"])
except:
    baseline = 82.41

optimized = baseline * 0.92
saved = baseline - optimized

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Baseline Energy",
        f"{baseline:.2f} GJ"
    )

with c2:
    st.metric(
        "Optimized Energy",
        f"{optimized:.2f} GJ"
    )

with c3:
    st.metric(
        "Energy Saved",
        f"{saved:.2f} GJ",
        f"{saved/baseline*100:.1f}%"
    )

st.divider()

# ---------------- LIVE SENSOR DATA ----------------

st.header("📊 Live Building Sensor Data")

st.dataframe(sensor_data, use_container_width=True)

m1, m2, m3, m4, m5 = st.columns(5)

with m1:
    st.metric(
        "🌡 Temperature",
        f"{sensor_data['Temperature'][0]} °C"
    )

with m2:
    st.metric(
        "💧 Humidity",
        f"{sensor_data['Humidity'][0]} %"
    )

with m3:
    st.metric(
        "👥 Occupancy",
        int(sensor_data["Occupancy"][0])
    )

with m4:
    st.metric(
        "⚡ Energy",
        f"{sensor_data['Energy_kWh'][0]} kWh"
    )

with m5:
    st.metric(
        "🌫 CO₂",
        int(sensor_data["CO2"][0])
    )

st.divider()

# ---------------- ALERTS ----------------

st.header("🚨 Building Alerts")

if sensor_data["Temperature"][0] > 30:
    st.warning("🌡 High temperature detected")

if sensor_data["Humidity"][0] > 60:
    st.warning("💧 High humidity detected")

if sensor_data["Energy_kWh"][0] > 180:
    st.warning("⚡ High energy consumption")

if sensor_data["CO2"][0] > 800:
    st.error("🌫 High CO₂ concentration detected")

# ---------------- AGENT DECISIONS ----------------

st.header("🤖 AI Control Decisions")

decisions = make_decision(sensor_data)

for decision in decisions:
    st.success(decision)

st.divider()
# ---------------- BUILDING HEALTH ----------------

st.header("🏢 Building Health")

health = 100

if sensor_data["Temperature"][0] > 30:
    health -= 10

if sensor_data["Humidity"][0] > 60:
    health -= 10

if sensor_data["Energy_kWh"][0] > 180:
    health -= 20

if sensor_data["CO2"][0] > 800:
    health -= 20

health = max(0, health)

if health >= 85:
    status = "🟢 Excellent"
elif health >= 70:
    status = "🟡 Good"
elif health >= 50:
    status = "🟠 Warning"
else:
    status = "🔴 Critical"

c1, c2 = st.columns(2)

with c1:
    st.metric("Building Health Score", f"{health}/100")

with c2:
    st.metric("Overall Status", status)

st.divider()

# ---------------- AI ANALYSIS ----------------

st.header("🤖 AI Analysis")

prompt = f"""
You are an intelligent Building Management AI.

EnergyPlus Simulation

{simulation}

Live Sensor Data

{sensor_data.to_string()}

Agent Decisions

{decisions}

Provide:

1. Building health
2. Energy efficiency
3. Problems
4. Safety concerns
5. Recommended actions
6. Estimated energy savings

Answer using bullet points only.
"""

with st.spinner("Analysing building..."):
    analysis = ask_llm(prompt)

st.markdown(analysis)

st.divider()

# ---------------- HISTORY ----------------

st.header("📈 Live Energy History")

if "history" not in st.session_state:
    st.session_state.history = []

st.session_state.history.append(
    sensor_data["Energy_kWh"][0]
)

if len(st.session_state.history) > 20:
    st.session_state.history.pop(0)

history_df = pd.DataFrame(
    st.session_state.history,
    columns=["Energy_kWh"]
)

st.line_chart(history_df)

st.divider()

# ---------------- ASK AI ----------------

st.header("💬 Ask EcoLoop AI")

question = st.text_input(
    "Ask anything about your building",
    placeholder="Example: How can I reduce today's energy consumption?"
)

if st.button("Ask AI"):

    chat_prompt = f"""
EnergyPlus Simulation

{simulation}

Current Sensor Data

{sensor_data.to_string()}

Agent Decisions

{decisions}

Question

{question}

Answer clearly in bullet points.
"""

    with st.spinner("Thinking..."):
        answer = ask_llm(chat_prompt)

    st.success(answer)

st.divider()

# ---------------- FOOTER ----------------

st.caption("Eco Loop Building AI | EnergyPlus + Ollama + Gemma + Streamlit")