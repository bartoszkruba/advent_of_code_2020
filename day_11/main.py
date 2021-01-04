with open('puzzle_inputs.txt') as f:
    inputs = [line.replace('\n', '') for line in f]


def adjacent_seats_version1(coordinates, pattern):
    count = 0
    for check in [(-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (0, 1), (1, 0)]:
        y = coordinates[0] + check[0]
        x = coordinates[1] + check[1]
        if y < 0 or y >= len(pattern) or x < 0 or x >= len(pattern[0]):
            continue
        if pattern[y][x] == '#':
            count += 1

    return count


def adjacent_seats_version2(coordinates, pattern):
    count = 0
    for check in [(-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (0, 1), (1, 0)]:
        temp = [coordinates[0], coordinates[1]]
        while True:
            temp[0] += check[0]
            temp[1] += check[1]
            y = temp[0]
            x = temp[1]
            if y < 0 or y >= len(pattern) or x < 0 or x >= len(pattern[0]):
                break

            if pattern[y][x] != '.':
                count += 1 if pattern[y][x] == '#' else 0
                break

    return count


def patterns_equal(new_pattern, old_pattern):
    for i in range(len(new_pattern)):
        if new_pattern[i] != old_pattern[i]:
            return False

    return True


def count_seats(pattern):
    count = 0
    for line in pattern:
        for letter in line:
            count += 1 if letter == '#' else 0
    return count


def simulation(inputs, algorithm, limit):
    old_pattern = inputs
    new_pattern = ['' for _ in old_pattern]

    while True:
        for i in range(len(old_pattern)):
            for j in range(len(old_pattern[i])):
                letter = old_pattern[i][j]
                if letter == '.':
                    new_pattern[i] += letter
                    continue

                neighbors = algorithm((i, j), old_pattern)
                if letter == 'L':
                    new_pattern[i] += '#' if neighbors == 0 else 'L'
                else:
                    new_pattern[i] += 'L' if neighbors >= limit else '#'

        if patterns_equal(new_pattern, old_pattern):
            break
        old_pattern = new_pattern
        new_pattern = ['' for _ in old_pattern]
    return count_seats(new_pattern)


def find_solution1(inputs):
    return simulation(inputs, adjacent_seats_version1, 4)


def find_solution2(inputs):
    return simulation(inputs, adjacent_seats_version2, 5)


print("Part one solution: ", find_solution1(inputs))

print("Part two solution: ", find_solution2(inputs))
