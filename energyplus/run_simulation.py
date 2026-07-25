import subprocess
import os

ENERGYPLUS_EXE = r"C:\EnergyPlusV26-1-0\energyplus.exe"

idf = os.path.abspath("energyplus/1ZoneUncontrolled.idf")
weather = os.path.abspath("energyplus/USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw")
output = os.path.abspath("energyplus/output")

subprocess.run([
    ENERGYPLUS_EXE,
    "-w", weather,
    "-d", output,
    idf
])

print("Simulation completed!")