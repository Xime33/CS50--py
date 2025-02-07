def main():
    spacecraft = {"name": "Voyager 1"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    =========REPORT===========

    Name: { spacecraft.get("name", "Unknown")}
    Distance: { spacecraft.get("distance","Unknown")} AU
    Orbit: { spacecraft.get("orbit", "Unknown")}

    ==========================
    """
main()


distances = {
    "Voyager 1": 163,
    "Voyager 2" : 136,
    "Pioneer 10" : 80,
    "New Horizons" : 58,
    "Pioneer 11" : 44
}

def main():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")

def convert(au):
    return au * 149597870700


main()
