import re
import itertools

with open('puzzle_inputs.txt') as f:
    inputs = [line.replace('\n', '') for line in f]


def write_value_1(mask, value):
    new_value = ''

    for i in range(len(mask)):
        if mask[i] != 'X':
            new_value += mask[i]
        else:
            new_value += value[i]

    return new_value


def write_value_2(mask, value):
    new_value = ''

    for i in range(len(mask)):
        if mask[i] != 'X':
            new_value += '1' if mask[i] == '1' or value[i] == '1' else '0'
        else:
            new_value += 'X'

    return new_value


def find_solution1(inputs):
    memory = {}
    mask = ''
    for input in inputs:

        if input[:4] == 'mask':
            mask = input.split('=')[1].replace(' ', '')
        elif input[:3] == 'mem':
            memory_addr = re.sub('[^0-9]', '', input.split('=')[0])
            value = "{0:b}".format(int(re.sub('[^0-9]', '', input.split('=')[1]))).zfill(36)
            new_value = write_value_1(mask, value)
            memory[memory_addr] = int(new_value, 2)

    sum = 0

    for key, value in memory.items():
        sum += value

    return sum


def find_solution2(inputs):
    memory = {}
    mask = ''
    for input in inputs:

        if input[:4] == 'mask':
            mask = input.split('=')[1].replace(' ', '')
        elif input[:3] == 'mem':
            memory_addr = re.sub('[^0-9]', '', input.split('=')[0])
            memory_bin = "{0:b}".format(int(memory_addr)).zfill(36)
            value = int(re.sub('[^0-9]', '', input.split('=')[1]))
            new_value = write_value_2(mask, memory_bin)

            floating = []

            for i in range(len(new_value)):
                if new_value[i] == 'X':
                    floating.append(2 ** (36 - i - 1))

            base = int(new_value.replace('X', '0'), 2)
            combinations = [list(zip(floating, x)) for x in itertools.product([True, False], repeat=len(floating))]
            addresses = []

            for combination in combinations:
                address = base
                for v, flag in combination:
                    address += int(v) if flag else 0
                memory[address] = value
                addresses.append(address)

    sum = 0

    for key, value in memory.items():
        sum += value

    return sum

find_solution2(inputs)

print('Part one solution: ', find_solution1(inputs))
print('Part two solution: ', find_solution2(inputs))
