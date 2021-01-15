tiles = {}

with open('puzzle_inputs.txt') as f:
    tile_id = None
    tile = []

    for line in f:
        line = line.replace('\n', '')
        if len(line) == 0:
            tiles[tile_id] = tile
            tile = []
        elif line[:4] == 'Tile':
            tile_id = int(line.replace('Tile', '').replace(' ', '').replace(':', ''))
        else:
            tile.append([c for c in line])
    tiles[tile_id] = tile


def rotate_2d_array(arr):
    return list(zip(*arr[::-1]))


def flip_horizontally(arr):
    new_arr = []
    i = len(arr) - 1

    while i >= 0:
        new_arr.append(arr[i])
        i -= 1
    return new_arr


def flip_vertically(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[i][::-1])
    return new_arr


def print_tile(tile):
    for line in tile:
        print(line)
    print('\n')


def match_top(tile1, tile2):
    return tile1[0] == tile2[-1]


def match_bottom(tile1, tile2):
    return tile1[-1] == tile2[0]


def match_right(tile1, tile2):
    return rotate_2d_array(tile1)[-1] == rotate_2d_array(tile2)[0]


def match_left(tile1, tile2):
    return rotate_2d_array(tile1)[0] == rotate_2d_array(tile2)[-1]


def tile_combinations(tiles):
    combinations = {}
    for key in tiles:
        for i in range(4):
            if i == 1:
                tile = flip_vertically(tiles[key])
            elif i == 2:
                tile = flip_horizontally(tiles[key])
            elif i == 3:
                tile = flip_horizontally(flip_vertically(tiles[key]))
            else:
                tile = tiles[key]
            for j in range(4):
                id = '{}|{}|{}'.format(key, i, j)
                tile = rotate_2d_array(tile)
                combinations[id] = tile
    return combinations


def find_matches(combinations):
    matches = {}
    for key1 in combinations:
        matches[key1] = {
            'top': set(),
            'right': set(),
            'bottom': set(),
            'left': set()
        }

        for key2 in combinations:
            if key1.split('|')[0] == key2.split('|')[0]:
                continue

            tile1 = combinations[key1]
            tile2 = combinations[key2]

            if match_top(tile1, tile2):
                matches[key1]['top'].add(key2)
            if match_right(tile1, tile2):
                matches[key1]['right'].add(key2)
            if match_bottom(tile1, tile2):
                matches[key1]['bottom'].add(key2)
            if match_left(tile1, tile2):
                matches[key1]['left'].add(key2)
    return matches


def find_solution1(tiles):
    ids = set()

    for key, value in find_matches(tile_combinations(tiles)).items():
        match_top = 1 if len(value['top']) > 0 else 0
        match_right = 1 if len(value['right']) > 0 else 0
        match_bottom = 1 if len(value['bottom']) > 0 else 0
        match_left = 1 if len(value['left']) > 0 else 0

        if match_top + match_right + match_bottom + match_left == 2:
            ids.add(int(key.split('|')[0])
                    )

    answer = 1
    for id in ids:
        answer *= id
    return answer


print('Part One Solution:', find_solution1(tiles))
