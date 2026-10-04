file = open("../data/input", "r")
tokens = file.read().splitlines()[0].split(',')
originalNums = list(map(int, tokens))
file.close()

for noun in range(100):
    for verb in range(100):
        nums = originalNums.copy()
        nums[1] = noun
        nums[2] = verb
        index = 0

        while nums[index] != 99:
            match nums[index]:
                case 1:
                    nums[nums[index + 3]] = nums[nums[index + 1]] + nums[nums[index + 2]]
                    index += 4
                case 2:
                    nums[nums[index + 3]] = nums[nums[index + 1]] * nums[nums[index + 2]]
                    index += 4

        if nums[0] == 19690720:
            break

    if nums[0] == 19690720:
        break

print("100 * noun + verb to produce output 19690720 is", 100 * noun + verb)
