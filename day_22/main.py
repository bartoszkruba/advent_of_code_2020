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


def calculate_score(deck):
    score = 0
    factor = 1

    for n in deck:
        score += n * factor
        factor += 1

    return score


def combat(deck_one, deck_two):
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

    return deck_one, deck_two


def recursive_combat(deck_one, deck_two, game=0):
    history = []
    game += 1

    round = 1

    while True:
        if len(deck_two) == 0:
            winner = 1
            break
        if len(deck_one) == 0:
            winner = 2
            break

        round += 1

        s = ''.join(str(card) for card in deck_one).join(str(card) for card in deck_two)

        if s in history:
            winner = 1
            break

        history.append(s)

        card_one = deck_one.pop()
        card_two = deck_two.pop()

        if card_one <= len(deck_one) and card_two <= len(deck_two):
            _, _, winner = recursive_combat(
                [card for card in deck_one[-card_one:]],
                [card for card in deck_two[-card_two:]],
                game
            )
            if winner == 1:
                deck_one.insert(0, card_one)
                deck_one.insert(0, card_two)
            else:
                deck_two.insert(0, card_two)
                deck_two.insert(0, card_one)
            continue

        if card_one > card_two:
            deck_one.insert(0, card_one)
            deck_one.insert(0, card_two)
        else:
            deck_two.insert(0, card_two)
            deck_two.insert(0, card_one)

    return deck_one, deck_two, winner


def find_solution1(deck_one, deck_two):
    deck_one, deck_two = combat([card for card in deck_one], [card for card in deck_two])

    return calculate_score(deck_one if len(deck_one) > 0 else deck_two)


def find_solution2(deck_one, deck_two):
    deck_one, deck_two, _ = recursive_combat([card for card in deck_one], [card for card in deck_two])

    return calculate_score(deck_one if len(deck_one) > 0 else deck_two)


print('Part One Solution:', find_solution1(deck_one, deck_two))
print('Part Two Solution:', find_solution2(deck_one, deck_two))
