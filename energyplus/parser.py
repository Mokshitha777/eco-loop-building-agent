import re

def read_summary(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    total_energy = "Unknown"

    match = re.search(r"Total Site Energy,([0-9.]+)", text)

    if match:
        total_energy = match.group(1)

    return {
        "Total Site Energy (GJ)": total_energy
    }