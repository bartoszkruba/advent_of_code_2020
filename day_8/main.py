with open('puzzle_inputs.txt') as f:
    inputs = [line.replace('\n', '') for line in f]


def parse_commands(inputs):
    return [[input.split(' ')[0], int(input.split(' ')[1])] for input in inputs]


def run_commands(commands):
    indexes = []
    index = 0
    accumulator = 0

    while index not in indexes and index < len(commands):
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

    return accumulator, True if index == len(commands) else False


def find_solution1(commands):
    return run_commands(commands)[0]


def find_solution2(commands):
    for i in range(len(commands)):
        command = commands[i][0]
        if command in ['jmp', 'nop']:
            commands[i][0] = 'nop' if command == 'jmp' else 'jmp'
            accumulator, correct = run_commands(commands)
            if correct:
                return accumulator
            else:
                commands[i][0] = command


commands = parse_commands(inputs)

print('Part one solution: ', find_solution1(commands))

print('Part two solution: ', find_solution2(commands))
