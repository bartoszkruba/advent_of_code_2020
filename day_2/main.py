inputs = []
for line in open('puzzle_inputs.txt'):
    inputs.append(line.replace("\n", ""))


def process_input(input):
    split = input.split(' ')
    return int(split[0].split('-')[0]), int(split[0].split('-')[1]), split[1][:-1], split[2]


# Part one
def find_solution1(inputs):
    count = 0
    for input in inputs:
        min, max, letter, password = process_input(input)
        occurrences = password.count(letter)

        if min <= occurrences <= max:
            count += 1

    return count


print("Part one solution:", find_solution1(inputs))


def find_solution2(inputs):
    count = 0
    for input in inputs:

        position1, position2, letter, password = process_input(input)
        position1 -= 1
        position2 -= 1
        matches = 0

        if len(password) > position1 and password[position1] == letter:
            matches += 1
        if len(password) > position2 and password[position2] == letter:
            matches += 1

        if matches == 1:
            count += 1

    return count


print('Part two solution:', find_solution2(inputs))
