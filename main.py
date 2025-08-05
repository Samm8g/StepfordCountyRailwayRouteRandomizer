import random

print("Stepford County Railway Route Randomizer")

stations = [
"Willowfield",
"Hemdon Park",
"Beechley",
"Financial Quarter",
"Stepford Victoria",
"City Hospital",
"Stepford Central",
"Four Ways",
"Stepford East",
"Stepford High Street",
"Whitefield Lido",
"Stepford UFC",
"Woodhead Lane",
"Houghton Rake",
"Whitefield",
"St. Helens Bridge",
"New Harrow",
"Elsemere Pond",
"Elsemere Junction",
"Berrily",
"East Berrily",
"Beaulieu Park",
"Morganstown",
"Angel Pass",
"Bodin",
"Coxly Newtown",
"Barton",
"Coxly",
"West Benton",
"Faraday Road",
"Eden Quay",
"Newry",
"Newry Harbour",
"Benton",
"Port Benton",
"Morganstown Docks",
"Whitney Green",
"Greenslade",
"Cambridge Street Parkway",
"Ashlan Park",
"Connolly",
"Airport West",
"James Street",
"Farleigh",
"Rosedale Village",
"Esterfield",
"Benton Bridge",
"Airport Parkway",
"Airport Central",
"Terminal 1",
"Terminal 2",
"Terminal 3",
"Hampton Hargate",
"Upper Staploe",
"Water Newton",
"Rocket Parade",
"Leighton Stepford Road",
"Leighton City",
"Leighton West",
"Aslockby",
"Carnalea Bridge",
"Rayleigh Bay",
"Edgemead",
"Faymere",
"Westercoast",
"Millcastle Racecourse",
"Millcastle",
"Westwyvern",
"Starryloch",
"Northshore",
"Llyn-by-the-Sea"
]

print("""
Difficulties:
1) Easiest
2) Easy
3) Normal
4) Hard
5) Hardest
""")

try:
    diff = int(input("Enter Difficulty (1-5): "))
    if 1 <= diff <= 5:
        random.seed(diff * 10)
        startPoint = random.choice(stations)
        endPoint = random.choice(stations)
        while endPoint == startPoint:
            endPoint = random.choice(stations)

        print(f"Starting station: {startPoint}")
        print(f"Ending station: {endPoint}")
    else:
        print("Please enter a number between 1 and 5.")
except ValueError:
    print("Invalid input. Please enter a number.")
