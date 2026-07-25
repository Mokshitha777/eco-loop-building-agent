from simulator.simulator import generate_building_data
from ai.llm import ask_llm
from test_energyplus import read_energy

from ai.agent import *

energy = read_energy()

print("\n========== ENERGYPLUS ==========\n")
print(energy)

data = generate_building_data()

print("\n========== LIVE SENSOR DATA ==========\n")
print(data)

analysis = ask_llm(data.to_string())

print("\n========== AI ANALYSIS ==========\n")
print(analysis)

clear_actions()

text = analysis.lower()

if "co2" in text:
    increase_ventilation()

if "lighting" in text:
    dim_lights()

if "cool" in text or "hvac" in text:
    reduce_hvac()

print("\n========== AI ACTIONS ==========\n")

for action in get_actions():
    print(action)