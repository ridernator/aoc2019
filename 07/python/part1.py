from enum import Enum
import itertools


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1


file = open("../data/input", "r")
originalNums = file.read().splitlines()[0].split(',')
file.close()

possiblePhaseSettings = [0, 1, 2, 3, 4]

permutations = itertools.permutations(possiblePhaseSettings)

highestSignal = 0

for phaseSettings in permutations:
    register = 0

    for phaseSetting in phaseSettings:
        phaseSettingRead = False
        nums = originalNums.copy()
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
                    if phaseSettingRead:
                        nums[int(nums[index + 1])] = register
                    else:
                        nums[int(nums[index + 1])] = phaseSetting
                        phaseSettingRead = True

                    index += 2

                case "4":
                    arg0 = int(nums[index + 1])
                    if mode0 == Mode.POSITION:
                        arg0 = int(nums[int(nums[index + 1])])

                    register = arg0

                    index += 2

                case "5":
                    arg0 = int(nums[index + 1])
                    if mode0 == Mode.POSITION:
                        arg0 = int(nums[int(nums[index + 1])])

                    arg1 = int(nums[index + 2])
                    if mode1 == Mode.POSITION:
                        arg1 = int(nums[int(nums[index + 2])])

                    if arg0 != 0:
                        index = arg1
                    else:
                        index += 3

                case "6":
                    arg0 = int(nums[index + 1])
                    if mode0 == Mode.POSITION:
                        arg0 = int(nums[int(nums[index + 1])])

                    arg1 = int(nums[index + 2])
                    if mode1 == Mode.POSITION:
                        arg1 = int(nums[int(nums[index + 2])])

                    if arg0 == 0:
                        index = arg1
                    else:
                        index += 3

                case "7":
                    arg0 = int(nums[index + 1])
                    if mode0 == Mode.POSITION:
                        arg0 = int(nums[int(nums[index + 1])])

                    arg1 = int(nums[index + 2])
                    if mode1 == Mode.POSITION:
                        arg1 = int(nums[int(nums[index + 2])])

                    if arg0 < arg1:
                        nums[int(nums[index + 3])] = "1"
                    else:
                        nums[int(nums[index + 3])] = "0"

                    index += 4

                case "8":
                    arg0 = int(nums[index + 1])
                    if mode0 == Mode.POSITION:
                        arg0 = int(nums[int(nums[index + 1])])

                    arg1 = int(nums[index + 2])
                    if mode1 == Mode.POSITION:
                        arg1 = int(nums[int(nums[index + 2])])

                    if arg0 == arg1:
                        nums[int(nums[index + 3])] = "1"
                    else:
                        nums[int(nums[index + 3])] = "0"

                    index += 4
                case _:
                    print("We broke!")

    if register > highestSignal:
        highestSignal = register

print("Highest final signal =", highestSignal)
