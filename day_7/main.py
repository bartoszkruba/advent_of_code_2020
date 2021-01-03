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
            color = split[1] + ' ' + split[2]
            rules[bag].append((number, color))

    return rules


def can_contain(rules, bag, color):
    if len(rules[bag]) == 0:
        return False

    for rule in rules[bag]:
        if rule[1] == color:
            return True
        elif can_contain(rules, rule[1], color):
            return True
    return False


def find_solution1(rules):
    count = 0
    for bag in rules:
        if bag != 'shiny gold' and can_contain(rules, bag, 'shiny gold'):
            count += 1
    return count


rules = parse_rules(inputs)

print('Part one solution:', find_solution1(rules))
