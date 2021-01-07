inputs = []
with open('puzzle_inputs.txt') as f:
    for line in f:
        for number in line.split(','):
            inputs.append(int(number.replace('\n', '')))


def find_solution1(inputs):
    # number spoken -> last turn the number was spoken
    numbers = {}
    last_spoken = None

    i = 0
    for number in inputs:
        if last_spoken is not None:
            numbers[last_spoken] = i - 1
        last_spoken = number
        i += 1

    while i < 2020:
        last_turn = i - 1
        if last_spoken not in numbers:
            new_last_spoken = 0
        else:
            new_last_spoken = last_turn - numbers[last_spoken]

        numbers[last_spoken] = last_turn
        last_spoken = new_last_spoken
        i += 1

    return last_spoken


print('Part one solution:', find_solution1(inputs))
