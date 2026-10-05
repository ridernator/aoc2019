file = open("../data/input", "r")
lines = file.read().splitlines()
file.close()

start = int(lines[0].split('-')[0])
stop = int(lines[0].split('-')[1])

count = 0
for num in range(start, stop + 1):
    incrementingNum = True
    numString = str(num)

    for index in range(1, len(numString)):
        if int(numString[index]) < int(numString[index - 1]):
            incrementingNum = False

            break

    if not incrementingNum:
        continue

    for index in range(0, len(numString)):
        groupSize = 1

        for back in range(index - 1, -1, -1):
            if numString[back] == numString[index]:
                groupSize += 1

        for fwd in range(index + 1, len(numString)):
            if numString[fwd] == numString[index]:
                groupSize += 1

        if groupSize == 2:
            count += 1

            break

print("Number of valid passwords =", count)
