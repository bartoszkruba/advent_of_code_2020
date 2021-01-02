with open('puzzle_inputs.txt') as f:
    inputs = [line.replace('\n', '') for line in f]


def parse_rules(inputs):
    rules = {}

    for input in inputs:
        split = input.split('contain')
        bag = split[0].replace('bags', '').strip()

        if bag not in rules:
            rules[bag] = []

        for rule in split[1].replace('\\s', '').replace('bags', '').replace('bag', '').replace('.', '').split(','):
            rule = rule.strip()
            if rule == 'no other':
                continue

            split = rule.split(' ')
            number = split[0]
            color = split[1] + split[2]
            rules[bag].append((number, color))


