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


print('Part one solution:', find_solution1(inputs))
