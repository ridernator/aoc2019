file = open("../data/input", "r")

masses = file.read().splitlines()

totalFuel = 0

for mass in masses:
    fuel = int(mass) // 3
    fuel -= 2
    totalFuel += fuel

print("Total fuel needed is ", totalFuel)
