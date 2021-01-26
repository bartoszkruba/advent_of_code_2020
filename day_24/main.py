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


def adjacent_tiles(tile):
    x = float(tile.split('|')[0])
    y = float(tile.split('|')[1])

    directions = [(1, 0), (0.5, -0.5), (-0.5, -0.5), (-1, 0), (-0.5, 0.5), (0.5, 0.5)]

    tiles = []

    for direction in directions:
        tiles.append(str(x + direction[0]) + '|' + str(y + direction[1]))

    return tiles


def count_adjacent_black_tiles(tile, black_tiles):
    adjacent = adjacent_tiles(tile)

    count = 0

    for tile in adjacent:
        if tile in black_tiles:
            count += 1

    return count


def find_solution1(inputs):
    return len(get_black_tiles(inputs))


def find_solution2(inputs):
    black_tiles = set(get_black_tiles(inputs))

    for _ in range(100):
        tiles_to_check = set()

        for tile in black_tiles:
            tiles_to_check.add(tile)
            for tile in adjacent_tiles(tile):
                tiles_to_check.add(tile)

        new_black_tiles = set()
        for tile in tiles_to_check:
            count = count_adjacent_black_tiles(tile, black_tiles)
            black = tile in black_tiles

            if (black and 0 < count <= 2) or (not black and count == 2):
                new_black_tiles.add(tile)

        black_tiles = new_black_tiles

    return len(black_tiles)


print('Part One Solution:', find_solution1(inputs))
print('Part Two Solution:', find_solution2(inputs))
