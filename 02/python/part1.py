file = open("../data/input", "r")
nums = list(map(int, file.read().splitlines()[0].split(',')))
file.close()

nums[1] = 12
nums[2] = 2

index = 0

while nums[index] != 99:
    match nums[index]:
        case 1:
            nums[nums[index + 3]] = nums[nums[index + 1]] + nums[nums[index + 2]]
            index += 4
        case 2:
            nums[nums[index + 3]] = nums[nums[index + 1]] * nums[nums[index + 2]]
            index += 4

print("Number at position 0 after program has run is ", nums[0])
