terrain = []

with open('puzzle_inputs.txt') as f:
    for line in f:
        terrain.append(line.replace("\n", ""))


def count_collisions(terrain, slope):
    width = len(terrain[0])
    height = len(terrain)

    pos = [0, 0]
    collisions = 0

    while pos[1] < height:
        if terrain[pos[1]][pos[0]] == '#':
            collisions += 1

        pos[0] += slope[0]
        pos[1] += slope[1]
        if pos[0] >= width:
            pos[0] = pos[0] % (width - 1) - 1

    return collisions


def find_solution1(terrain):
    return count_collisions(terrain, (3, 1))


print("Part one solution: ", find_solution1(terrain))


def find_solution2(terrain):
    answer = 1

    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        answer *= count_collisions(terrain, slope)

    return answer


print("Part two solution: ", find_solution2(terrain))
