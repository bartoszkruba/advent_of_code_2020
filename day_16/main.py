with open('puzzle_inputs.txt') as f:
    section = 0
    rules = {}
    own_ticket = []
    others_tickets = []
    for line in f:
        line = line.replace('\n', '')
        if len(line) == 0:
            section += 1
        elif section == 0:
            split = line.split(':')
            rules[split[0]] = []
            for rule in split[1].split('or'):
                min = int(rule.split('-')[0])
                max = int(rule.split('-')[1])
                rules[split[0]].append((min, max))
        elif section == 1 and line != 'your ticket:':
            own_ticket = [int(number) for number in line.split(',')]
        elif section == 2 and line != 'nearby tickets:':
            others_tickets.append([int(number) for number in line.split(',')])


def valid_for_some_rule(number, rules):
    for rule in rules:
        if rule[0] <= number <= rule[1]:
            return True
    return False


def invalid_values(ticket, rules):
    all_rules = []
    for rules in [rules[key] for key in rules]:
        all_rules += rules
    invalid_values = []

    for value in ticket:
        if not (valid_for_some_rule(value, all_rules)):
            invalid_values.append(value)

    return invalid_values


def index_with_single_label(possibilities, ignore=[]):
    for key in possibilities:
        if len(possibilities[key]) == 1 and key not in ignore:
            return key


def find_solution1(tickets, rules):
    all_invalid_values = []
    for ticket in tickets:
        all_invalid_values += invalid_values(ticket, rules)
    return sum(all_invalid_values)


def find_solution2(own_ticket, others_tickets, rules):
    valid_tickets = []
    for ticket in others_tickets:
        if len(invalid_values(ticket, rules)) == 0:
            valid_tickets.append(ticket)
    valid_tickets.append(own_ticket)

    possibilities = {}
    for i in range(len(own_ticket)):
        possibilities[i] = [key for key in rules]

    for i in range(len(own_ticket)):
        for key in rules:
            r = rules[key]
            for ticket in valid_tickets:
                value = ticket[i]
                valid = valid_for_some_rule(value, r)
                if not valid:
                    possibilities[i].remove(key)
                    break

    ignore = []
    while index_with_single_label(possibilities, ignore) is not None:
        index = index_with_single_label(possibilities, ignore)
        ignore.append(index)
        label = possibilities[index][0]
        for key in possibilities:
            if key not in ignore and label in possibilities[key]:
                possibilities[key].remove(label)

    result = 1
    for key in possibilities:
        label = possibilities[key][0]
        if label.startswith('departure'):
            result *= own_ticket[key]

    return result


print('Solution for part one:', find_solution1(others_tickets, rules))
print('Solution for part two:', find_solution2(own_ticket, others_tickets, rules))
