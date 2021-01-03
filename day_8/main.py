with open('puzzle_inputs.txt') as f:
    inputs = [line.replace('\n', '') for line in f]


def parse_commands(inputs):
    return [(input.split(' ')[0], int(input.split(' ')[1])) for input in inputs]


def find_solution1(commands):
    indexes = []
    index = 0
    accumulator = 0

    while index not in indexes:
        command = commands[index][0]
        value = commands[index][1]

        if command == 'jmp':
            indexes.append(index)
            index += value
            continue
        elif command == 'acc':
            accumulator += value

        indexes.append(index)
        index += 1
    return accumulator


commands = parse_commands(inputs)

print('Part one solution: ', find_solution1(commands))
