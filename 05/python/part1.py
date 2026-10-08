from enum import Enum

class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1


register = 1

file = open("../data/input", "r")
nums = file.read().splitlines()[0].split(',')
file.close()

index = 0
while nums[index] != "99":
    opCode = nums[index][-1]
    mode0 = Mode.POSITION
    mode1 = Mode.POSITION

    if len(nums[index]) > 2:
        mode0 = Mode(int(nums[index][-3:-2]))

    if len(nums[index]) > 3:
        mode1 = Mode(int(nums[index][-4:-3]))

    match opCode:
        case "1":
            arg0 = int(nums[index + 1])
            if mode0 == Mode.POSITION:
                arg0 = int(nums[int(nums[index + 1])])

            arg1 = int(nums[index + 2])
            if mode1 == Mode.POSITION:
                arg1 = int(nums[int(nums[index + 2])])

            nums[int(nums[index + 3])] = str(arg0 + arg1)

            index += 4
        case "2":
            arg0 = int(nums[index + 1])
            if mode0 == Mode.POSITION:
                arg0 = int(nums[int(nums[index + 1])])

            arg1 = int(nums[index + 2])
            if mode1 == Mode.POSITION:
                arg1 = int(nums[int(nums[index + 2])])

            nums[int(nums[index + 3])] = str(arg0 * arg1)

            index += 4
        case "3":
            nums[int(nums[index + 1])] = register

            index += 2
        case "4":
            register = nums[int(nums[index + 1])]

            index += 2
        case _:
            print("We broke!")

print("Final output code is", register)
