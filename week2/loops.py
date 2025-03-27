bikes = ["Mountain", "Road", "Hybrid", "Electric"]
guitars = ["Acoustic", "Electric", "Bass"]
vehicles = {
    "Fusion": "Car",
    "F-150": "Truck",
    "4Runner": "SUV",
}

sports = [
    {
        "name": "Running",
        "team_size": None
    },
    {
        "name": "Basketball",
        "team_size": 5,
    },
]

for bike in bikes:
    print(bike)

for i in range(len(guitars)):
    print(guitars[i], i)

for vehicle in vehicles:
    print(vehicle, vehicles[vehicle], sep=", ")

for sport in sports:
    print(sport["name"], sport["team_size"], sep=", ")