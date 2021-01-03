with open('puzzle_inputs.txt') as f:
    inputs = [int(line) for line in f]
    inputs.sort()


def find_solution1(inputs):
    joltages = [0] + inputs + [inputs[len(inputs) - 1] + 3]
    i = 0
    j = 1

    differences = {
        1: 0,
        3: 0
    }

    while j < len(joltages):
        difference = joltages[j] - joltages[i]
        if difference == 1:
            differences[1] += 1
        elif difference == 3:
            differences[3] += 1
        i += 1
        j += 1

    return differences[1] * differences[3]


def find_possible_next_adapters(number, inputs):
    possibilities = []
    for possibility in [number + 1, number + 2, number + 3]:
        if possibility in inputs:
            possibilities.append(possibility)
    return possibilities


# Counting combination by creating "node tree"
# Each step in while loop is a next level in the tree
def find_solution2(inputs):
    count = 0

    nodes = {input: 1 if input == 0 else 0 for input in [0] + inputs}

    while sum(nodes.values()) != 0:
        count += nodes[inputs[-1]]
        new_nodes = {input: 0 for input in [0] + inputs}

        for node in nodes:
            for number in find_possible_next_adapters(node, inputs):
                new_nodes[number] += nodes[node]
        nodes = new_nodes

    return count


print('Part one solution:', find_solution1(inputs))

print('Part two solution:', find_solution2(inputs))
