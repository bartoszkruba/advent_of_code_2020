with open('puzzle_inputs.txt') as f:
    inputs = [line.replace('\n', '') for line in f]


def find_row(input):
    rows = [i for i in range(128)]

    for command in input[:7]:
        rows = rows[:len(rows) // 2] if command == 'F' else rows[-len(rows) // 2:]
    return rows[0]


def find_column(input):
    columns = [i for i in range(8)]

    for command in input[7:]:
        columns = columns[:len(columns) // 2] if command == 'L' else columns[-len(columns) // 2:]
    return columns[0]


def find_solution1(inputs):
    highest = 0
    for input in inputs:
        row = find_row(input)
        column = find_column(input)
        id = row * 8 + column
        highest = id if (highest < id) else highest
    return highest


print("Part one solution: ", find_solution1(inputs))


def find_solution2(inputs):
    ids = [find_row(input) * 8 + find_column(input) for input in inputs]
    ids.sort()
    for i in range(len(ids) - 1):
        if ids[i] + 1 != (ids[i + 1]):
            return ids[i] + 1


print("Part two solution: ", find_solution2(inputs))
