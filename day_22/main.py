deck_one = []
deck_two = []

section = 0

with open('puzzle_inputs.txt') as f:
    for line in f:
        line = line.replace('\n', '')

        if 'Player' in line:
            continue
        elif len(line) == 0:
            section += 1
            continue

        if section == 0:
            deck_one.insert(0, int(line))
        else:
            deck_two.insert(0, int(line))


def find_solution1(deck_one, deck_two):
    while True:
        card_one = deck_one.pop()
        card_two = deck_two.pop()

        if card_one > card_two:
            deck_one.insert(0, card_one)
            deck_one.insert(0, card_two)
        else:
            deck_two.insert(0, card_two)
            deck_two.insert(0, card_one)

        if len(deck_one) == 0 or len(deck_two) == 0:
            break

    answer = 0
    factor = 1

    for n in deck_one if len(deck_one) > 0 else deck_two:
        answer += n * factor
        factor += 1

    return answer


print('Part One Solution:', find_solution1(deck_one, deck_two))
