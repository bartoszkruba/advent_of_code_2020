with open('puzzle_inputs.txt') as f:
    inputs = [int(line) for line in f]


def valid_number(number, previous):
    for i in range(len(previous)):
        for j in range(i + 1, len(previous)):
            if previous[i] + previous[j] == number:
                return True
    return False


def find_solution1(inputs):
    for i in range(25, len(inputs)):
        number = inputs[i]
        if not valid_number(number, inputs[i - 25:i]):
            return number


def find_solution2(inputs, target):
    for i in range(len(inputs)):
        for j in range(i + 1, len(inputs)):
            list = inputs[i:j + 1]
            s = sum(list)
            if s > target:
                break
            elif s == target:
                list.sort()
                return list[0] + list[len(list) - 1]


solution1 = find_solution1(inputs)
print('Part one solution:', solution1)

print('Part two solution:', find_solution2(inputs, solution1))
