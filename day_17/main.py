with open('puzzle_inputs.txt') as f:
    inputs = [line.replace('\n', '') for line in f]


def create_cube(shape, content=0):
    cube = []
    for z in range(shape[0]):
        col = []
        for y in range(shape[1]):
            row = []
            for x in range(shape[2]):
                row.append(content)
            col.append(row)
        cube.append(col)
    return cube


def create_permutations():
    permutations = []

    for z in (0, -1, 1):
        for y in (0, -1, 1):
            for x in (0, -1, 1):
                permutations.append((y, x, z))
    permutations.remove((0, 0, 0))
    return permutations


# def print_cube(cube):
#     z = 0
#     for arr in cube:
#         print('\n')
#         print('z:', z - middle_z)
#         z += 1
#         for line in arr:
#             print(line)


def neighbours_count(coordinates, permutations, cube):
    count = 0
    for p in permutations:
        try:
            if cube[coordinates[0] + p[0]][coordinates[1] + p[1]][coordinates[2] + p[2]] == 1:
                count += 1
            if count >= 4:
                return count
        except:
            pass
    return count


def active_field_count(cube):
    total = 0

    for z in range(len(cube)):
        for y in range(len(cube[0])):
            for x in range(len(cube[0][0])):
                total += cube[z][y][x]
    return total


def find_solution1(inputs):
    cycles = 6
    shape = [1 + 2 * cycles, len(inputs) + 2 * cycles, len(inputs[0]) + 2 * cycles]

    cube = create_cube(shape)
    middle_z = int(shape[0] / 2)
    middle_y = int(shape[1] / 2)
    middle_x = int(shape[2] / 2)
    for y in range(middle_y - int(len(inputs) / 2), middle_y - int(len(inputs) / 2) + len(inputs)):
        for x in range(middle_x - int(len(inputs[0]) / 2), middle_y - int(len(inputs) / 2) + len(inputs)):
            little_y = y - (middle_y - int(len(inputs) / 2))
            little_x = x - (middle_x - int(len(inputs[0]) / 2))
            cube[middle_z][y][x] = 1 if inputs[little_y][little_x] == '#' else 0

    new_cube = create_cube(shape)
    permutations = create_permutations()

    for n in range(cycles):
        for z in range(shape[0]):
            for y in range(shape[1]):
                for x in range(shape[2]):
                    coordinates = (z, y, x)
                    count = neighbours_count(coordinates, permutations, cube)
                    value = cube[z][y][x]
                    if count < 2:
                        new_value = 0
                    elif value == 1 and count in [2, 3]:
                        new_value = 1
                    elif value == 0 and count == 3:
                        new_value = 1
                    else:
                        new_value = 0
                    new_cube[z][y][x] = new_value

        cube, new_cube = new_cube, cube

    return active_field_count(cube)


print('Part one solution:', find_solution1(inputs))
