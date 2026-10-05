file = open("../data/input", "r")
lines = file.read().splitlines()
file.close()

start = int(lines[0].split('-')[0])
stop = int(lines[0].split('-')[1])

count = 0
for num in range(start, stop + 1):
    doubleFound = False
    incrementingNum = True
    numString = str(num)

    for index in range(1, len(numString)):
        if int(numString[index]) < int(numString[index - 1]):
            incrementingNum = False

            break

        if numString[index] == numString[index - 1]:
            doubleFound = True

    if doubleFound & incrementingNum:
        count += 1

print("Number of valid passwords =", count)
