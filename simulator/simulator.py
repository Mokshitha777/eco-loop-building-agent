import random
import pandas as pd


def generate_building_data():
    data = {
        "Temperature": round(random.uniform(20, 32), 2),
        "Humidity": round(random.uniform(35, 70), 2),
        "Occupancy": random.randint(0, 120),
        "Energy_kWh": round(random.uniform(60, 220), 2),
        "CO2": random.randint(350, 1200)
    }

    return pd.DataFrame([data])