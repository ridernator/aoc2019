file = open("../data/input", "r")

masses = file.read().splitlines()

totalFuel = 0

for mass in masses:
    fuel = int(mass) // 3
    fuel -= 2

    while fuel >= 0:
        totalFuel += fuel
        fuel = fuel // 3
        fuel -= 2

print("Total fuel needed is ", totalFuel)
