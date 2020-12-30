terrain = []

with open('puzzle_inputs.txt') as f:
    for line in f:
        terrain.append(line.replace("\n", ""))


def find_solution1(terrain):
    width = len(terrain[0])
    height = len(terrain)

    pos = [0, 0]
    collisions = 0

    while pos[1] < height:
        if terrain[pos[1]][pos[0]] == '#':
            collisions += 1

        pos[0] += 3
        pos[1] += 1
        if pos[0] >= width:
            pos[0] = pos[0] % (width - 1) - 1

    return collisions


print("Part one solution: ", find_solution1(terrain))
