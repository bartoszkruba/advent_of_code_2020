with open('puzzle_inputs.txt') as f:
    inputs = [int(line) for line in f]
    inputs.sort()


def find_solution1(inputs):
    joltages = [0] + inputs + [inputs[len(inputs) - 1] + 3]
    i = 0
    j = 1

    differences = {
        1: 0,
        3: 0
    }

    while j < len(joltages):
        difference = joltages[j] - joltages[i]
        if difference == 1:
            differences[1] += 1
        elif difference == 3:
            differences[3] += 1
        i += 1
        j += 1

    return differences[1] * differences[3]


print('Part one solution:', find_solution1(inputs))
