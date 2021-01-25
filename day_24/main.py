inputs = [line.replace('\n', '') for line in open('puzzle_inputs.txt')]


def get_black_tiles(inputs):
    possible_commands = ['e', 'se', 'sw', 'w', 'nw', 'ne']

    command_to_coords = {
        'e': (1, 0),
        'se': (0.5, -0.5),
        'sw': (-0.5, -0.5),
        'w': (-1, 0),
        'nw': (-0.5, 0.5),
        'ne': (0.5, 0.5)
    }

    black_tiles = []

    for input in inputs:
        s = ''
        commands = []

        for c in input:
            s += c

            if s in possible_commands:
                commands.append(s)
                s = ''

        coordinates = [0, 0]

        for command in commands:
            coords = command_to_coords[command]

            coordinates[0] += coords[0]
            coordinates[1] += coords[1]

        s = str(coordinates[0]) + '|' + str(coordinates[1])
        if s in black_tiles:
            black_tiles.remove(s)
        else:
            black_tiles.append(s)

    return black_tiles


def find_solution1(inputs):
    return len(get_black_tiles(inputs))


print('Part One Solution:', find_solution1(inputs))
