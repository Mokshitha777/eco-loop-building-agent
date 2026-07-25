def make_decision(data):
    decisions = []

    if data["Energy_kWh"][0] > 150:
        decisions.append("Enable Energy Saving Mode")

    if data["Temperature"][0] > 28:
        decisions.append("Turn ON Air Conditioning")

    if data["Temperature"][0] < 20:
        decisions.append("Turn OFF Air Conditioning")

    if data["Occupancy"][0] == 0:
        decisions.append("Turn OFF Lights")

    if data["CO2"][0] > 800:
        decisions.append("Increase Ventilation")

    if len(decisions) == 0:
        decisions.append("Everything is operating normally.")

    return decisions