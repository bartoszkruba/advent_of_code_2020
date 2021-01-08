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


def create_hyper_cube(shape, content=0):
    cube = []
    for w in range(shape[0]):
        cube.append(create_cube(shape[1:]))
    return cube


def create_permutations():
    permutations = []

    for z in (0, -1, 1):
        for y in (0, -1, 1):
            for x in (0, -1, 1):
                permutations.append((y, x, z))
    permutations.remove((0, 0, 0))
    return permutations


def create_4d_permutations():
    permutations = []

    for w in (0, -1, 1):
        for z in (0, -1, 1):
            for y in (0, -1, 1):
                for x in (0, -1, 1):
                    permutations.append((w, y, x, z))
    permutations.remove((0, 0, 0, 0))

    return permutations


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


def neighbours_count_4d(coordinates, permutations, cube):
    count = 0
    for p in permutations:
        try:
            if cube[coordinates[0] + p[0]][coordinates[1] + p[1]][coordinates[2] + p[2]][coordinates[3] + p[3]] == 1:
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


def active_field_count_4d(cube):
    total = 0

    for w in range(len(cube)):
        for z in range(len(cube[0])):
            for y in range(len(cube[0][0])):
                for x in range(len(cube[0][0][0])):
                    total += cube[w][z][y][x]
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


def find_solution2(inputs):
    cycles = 6
    shape = [1 + 2 * cycles, 1 + 2 * cycles, len(inputs) + 2 * cycles, len(inputs[0]) + 2 * cycles]
    cube = create_hyper_cube(shape)
    middle_w = int(shape[0] / 2)
    middle_z = int(shape[1] / 2)
    middle_y = int(shape[2] / 2)
    middle_x = int(shape[3] / 2)

    for y in range(middle_y - int(len(inputs) / 2), middle_y - int(len(inputs) / 2) + len(inputs)):
        for x in range(middle_x - int(len(inputs[0]) / 2), middle_y - int(len(inputs) / 2) + len(inputs)):
            little_y = y - (middle_y - int(len(inputs) / 2))
            little_x = x - (middle_x - int(len(inputs[0]) / 2))
            cube[middle_w][middle_z][y][x] = 1 if inputs[little_y][little_x] == '#' else 0

    new_cube = create_hyper_cube(shape)
    permutations = create_4d_permutations()

    for n in range(cycles):
        for w in range(shape[0]):
            for z in range(shape[1]):
                for y in range(shape[2]):
                    for x in range(shape[3]):
                        coordinates = (w, z, y, x)
                        count = neighbours_count_4d(coordinates, permutations, cube)
                        value = cube[w][z][y][x]

                        if count < 2:
                            new_value = 0
                        elif value == 1 and count in [2, 3]:
                            new_value = 1
                        elif value == 0 and count == 3:
                            new_value = 1
                        else:
                            new_value = 0
                        new_cube[w][z][y][x] = new_value
        cube, new_cube = new_cube, cube
    return active_field_count_4d(cube)


print('Part one solution:', find_solution1(inputs))
print('Part two solution:', find_solution2(inputs))
