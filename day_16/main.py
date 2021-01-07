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


def find_solution1(tickets, rules):
    all_invalid_values = []
    for ticket in tickets:
        all_invalid_values += invalid_values(ticket, rules)
    return sum(all_invalid_values)


print('Part one solution:', find_solution1(others_tickets, rules))
