inputs = []
for line in open('puzzle_inputs.txt'):
    inputs.append(int(line))


# Part one
def find_solution1(inputs):
    for i in range(len(inputs)):
        for j in range(i + 1, len(inputs)):
            if inputs[i] + inputs[j] == 2020:
                return inputs[i] * inputs[j]


print('Part one solution:', find_solution1(inputs))


# Part two
def find_solution2(inputs):
    for i in range(len(inputs)):
        for j in range(i + 1, len(inputs)):
            for k in range(j + 1, len(inputs)):
                if inputs[i] + inputs[j] + inputs[k] == 2020:
                    return inputs[i] * inputs[j] * inputs[k]


print('Part two solution:', find_solution2(inputs))
