from math import cos, sin, radians

with open('puzzle_inputs.txt') as f:
    inputs = [line.replace('\n', '') for line in f]


def parse_commands(inputs):
    return [(input[0], int(input[1:])) for input in inputs]


def find_solution1(commands):
    direction = 90
    pos = [0, 0]

    for command in commands:
        instruction = command[0]
        value = command[1]

        if instruction == 'N':
            pos[1] += value
        elif instruction == 'S':
            pos[1] -= value
        elif instruction == 'E':
            pos[0] += value
        elif instruction == 'W':
            pos[0] -= value
        elif instruction == 'L':
            direction = (direction - value) % 360
        elif instruction == 'R':
            direction = (direction + value) % 360
        elif instruction == 'F':
            pos[0] += int(sin(radians(direction))) * value
            pos[1] += int(cos(radians(direction))) * value

    return abs(pos[0]) + abs(pos[1])


commands = parse_commands(inputs)

print("Part one solution: ", find_solution1(commands))
