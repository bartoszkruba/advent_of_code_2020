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


def print_grid(grid):
    for arr in grid:
        for t in arr:
            id = '________' if t is None else t
            print(id, end=' ')
        print()


def print_image(image):
    for arr in image:
        for c in arr:
            print(c + '  ', end='')
        print()


def count_occurences(symbol, image):
    count = 0
    for arr in image:
        for c in arr:
            if c == symbol:
                count += 1
    return count


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
            for j in range(2):
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


def find_corners(tiles):
    corners = set()
    combinations = tile_combinations(tiles)
    matches = find_matches(combinations)

    for key, value in matches.items():
        match_top = 1 if len(value['top']) > 0 else 0
        match_right = 1 if len(value['right']) > 0 else 0
        match_bottom = 1 if len(value['bottom']) > 0 else 0
        match_left = 1 if len(value['left']) > 0 else 0

        if match_top + match_right + match_bottom + match_left == 2:
            corners.add(key)

    return corners, matches, combinations


def fill_image(image, combinations, grid):
    for i in range(len(image)):
        line = []
        for j in range(len(grid)):
            line += combinations[grid[i // 8][j]][i % 8 + 1][1:9]
        image[i] = line


def find_monster(start_coords, monster, image):
    for k in range(4):
        if k == 0:
            m = monster
        elif k == 1:
            m = flip_vertically(monster)
        elif k == 2:
            m = flip_horizontally(monster)
        else:
            m = flip_vertically(flip_horizontally(monster))

        match = True
        for i in range(len(monster)):
            for j in range(len(monster[0])):

                if m[i][j] == 'O' and image[start_coords[0] + i][start_coords[1] + j] != '#':
                    match = False

        if match:
            return True

    return False


def find_solution1(corners):
    filtered_ids = set()
    for id in corners:
        filtered_ids.add(int(id.split('|')[0]))

    answer = 1
    for id in filtered_ids:
        answer *= id

    return answer


def find_solution2(corners, matches, combinations, tiles):
    grid_size = int(len(tiles) ** 0.5)

    grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]

    for id in corners:
        m = matches[id]

        top_left = len(m['right']) > 0 and len(m['bottom']) > 0
        if top_left:
            grid[0][0] = id

    for i in range(1, grid_size):
        grid[i][0] = list(matches[grid[i - 1][0]]['bottom'])[0]

    for i in range(grid_size):
        for j in range(1, grid_size):
            grid[i][j] = list(matches[grid[i][j - 1]]['right'])[0]

    image_size = 8 * grid_size
    image = [['x' for _ in range(image_size)] for _ in range(image_size)]
    fill_image(image, combinations, grid)

    sea_monster = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'O', '.'],
        ['O', '.', '.', '.', '.', 'O', 'O', '.', '.', '.', '.', 'O', 'O', '.', '.', '.', '.', 'O', 'O', 'O'],
        [',', 'O', '.', '.', 'O', '.', '.', 'O', '.', '.', 'O', '.', '.', 'O', '.', '.', 'O', '.', '.', '.'],
    ]

    count = 0
    for _ in range(2):
        sea_monster = rotate_2d_array(sea_monster)
        for i in range(0, image_size - len(sea_monster) + 1):
            for j in range(0, image_size - len(sea_monster[0]) + 1):
                if find_monster((i, j), sea_monster, image):
                    count += 1

    return count_occurences('#', image) - count * count_occurences('O', sea_monster)


corners, matches, combinations = find_corners(tiles)

print('Part One Solution:', find_solution1(corners))
print('Part Two Solution:', find_solution2(corners, matches, combinations, tiles))
