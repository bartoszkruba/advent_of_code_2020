inputs = []
with open('puzzle_inputs.txt') as f:
    for line in f:
        for number in line.split(','):
            inputs.append(number.replace('\n', ''))


def find_solution1(inputs):
    target = int(inputs[0])
    timestamps = {}

    for id in inputs[1:]:
        if id == 'x':
            continue
        timestamp = int(id)

        while timestamp < target:
            timestamp += int(id)
        timestamps[id] = timestamp

    id = min(timestamps, key=timestamps.get)
    diff = timestamps[id] - target
    return int(id) * diff


def find_solution2(inputs):
    data = []

    for i in range(1, len(inputs)):

        if inputs[i] != 'x':
            data.append((int(inputs[i]), i - 1))

    data = sorted(data, key=lambda tup: tup[0], reverse=True)

    i = data[0][0]
    increment = data[0][0]

    for k in range(2, len(data) + 1):
        d = []
        while True:
            for j in range(k):
                target = i - data[0][1] + data[j][1]

                if int(target % data[j][0]) != 0:
                    break
            else:
                d.append(i)
                if len(d) >= 2:
                    increment = d[1] - d[0]
                    if k == len(data):
                        return d[0] - data[0][1]
                    break

            i += increment


print('Part one solution: ', find_solution1(inputs))

print('Part two solution: ', find_solution2(inputs))
