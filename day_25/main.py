part = 0

with open('puzzle_inputs.txt') as f:
    for line in f:
        if part == 0:
            doors_public_key = int(line.replace('\n', ''))
        else:
            cards_public_key = int(line.replace('\n', ''))
        part += 1


def encrypt(subject_number, loop_size):
    value = 1

    for _ in range(loop_size):
        value *= subject_number
        value %= 20201227

    return value


def find_loop_size(public_key):
    i = 1
    value = 1
    while True:
        value *= 7
        value %= 20201227
        if value == public_key:
            return i

        i += 1


def find_solution1(cards_public_key, doors_public_key):
    cards_loop_size = find_loop_size(cards_public_key)

    return encrypt(doors_public_key, cards_loop_size)


print('Part One Solution:', find_solution1(cards_public_key, doors_public_key))
