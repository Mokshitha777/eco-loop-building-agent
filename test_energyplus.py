from energyplus.parser import read_summary

data = read_summary("energyplus/output/eplustbl.csv")

print(data)