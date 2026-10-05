file = open("../data/input", "r")
lines = file.read().splitlines()
wire1Steps = lines[0].split(',')
wire2Steps = lines[1].split(',')
file.close()

wire1Positions: set[tuple[int, int]] = []
wire2Positions: set[tuple[int, int]] = []
wire1Distances: dict[tuple[int, int], int] = {}
wire2Distances: dict[tuple[int, int], int] = {}

x = 0
y = 0
distance = 0
for step in wire1Steps:
    count = int(step[1:])
    for index in range(1, count + 1):
        match step[0]:
            case 'R':
                x += 1
            case 'L':
                x -= 1
            case 'U':
                y += 1
            case 'D':
                y -= 1
        distance += 1
        wire1Positions.append((x, y))
        wire1Distances[(x, y)] = distance

x = 0
y = 0
distance = 0
for step in wire2Steps:
    count = int(step[1:])
    for index in range(1, count + 1):
        match step[0]:
            case 'R':
                x += 1
            case 'L':
                x -= 1
            case 'U':
                y += 1
            case 'D':
                y -= 1
        distance += 1
        wire2Positions.append((x, y))
        wire2Distances[(x, y)] = distance

crossings = list(set(wire1Positions) & set(wire2Positions))

minDistance = 10000000
for crossing in crossings:
    if minDistance > wire1Distances[(crossing[0], crossing[1])] + wire2Distances[(crossing[0], crossing[1])]:
        minDistance = wire1Distances[(crossing[0], crossing[1])] + wire2Distances[(crossing[0], crossing[1])]

print("Closet crossing to central port is at distance", minDistance)
