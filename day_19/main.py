import re

rules = {}
messages = []
section = 0
with open('puzzle_inputs.txt') as f:
    for line in f:
        line = line.replace('\n', '')
        if len(line) == 0:
            section += 1
            continue
        elif section == 0:
            rules[line.split(':')[0]] = line.split(':')[1].strip()
        else:
            messages.append(line)


def replace_rules(str, rules):
    arr = ['']
    s = ''
    for c in str:
        if c == ' ':
            if s not in rules:
                for i in range(len(arr)):
                    arr[i] += s + ' '
                s = ''
                continue

            r = rules[s]
            if '|' in r:
                new_arr = []
                for z in arr:
                    for n in r.split('|'):
                        new_arr.append(z + n.strip())
                arr = new_arr
            else:
                for i in range(len(arr)):
                    arr[i] += r
            s = ''
            for i in range(len(arr)):
                arr[i] += ' '
        else:
            s += c

    if s not in rules:
        for i in range(len(arr)):
            arr[i] += s
        return arr
    r = rules[s]
    if '|' in r:
        new_arr = []
        for z in arr:
            for n in r.split('|'):
                new_arr.append(z + n)
        arr = new_arr
    else:
        for i in range(len(arr)):
            arr[i] += r
    return arr


def find_solution1(messages, first_part_rules, second_part_rules):
    counter = 0
    for message in messages:
        if good_message_part1(message, first_part_rules, second_part_rules):
            counter += 1

    return counter


def find_solution2(messages, first_part_rules, second_part_rules):
    counter = 0
    for message in messages:
        if good_message_part2(message, first_part_rules, second_part_rules):
            counter += 1

    return counter


def generate_rules(rules, rule_start):
    arr = [rules[rule_start]]
    while True:
        count = 0
        new_arr = []
        for s1 in arr:
            for s2 in replace_rules(s1, rules):
                count += 1
                new_arr.append(s2)
        if arr == new_arr:
            break
        arr = new_arr

    for i in range(len(arr)):
        arr[i] = arr[i].replace('"', '').replace(' ', '')

    return arr


def good_message_part1(message, first_part_rules, second_part_rules):
    p_len = len(list(first_part_rules)[0])

    if len(message) != 3 * p_len:
        return False

    start = message[:p_len]
    middle = message[p_len: 2 * p_len]
    end = message[2 * p_len: 3 * p_len]

    return start in first_part_rules and middle in first_part_rules and end in second_part_rules


def good_message_part2(message, first_part_rules, second_part_rules):
    p_len = len(list(first_part_rules)[0])
    min_len = 3 * p_len

    good = True

    if len(message) < min_len or len(message) % p_len != 0:
        good = False
    elif message[-p_len:] not in second_part_rules:
        good = False
    elif message[0:p_len] not in first_part_rules or message[p_len: 2 * p_len] not in first_part_rules:
        good = False

    i = 0
    first_part = True
    first_part_count = 0
    second_part_count = 0
    while i <= len(message) - p_len:
        part = message[i: i + p_len]
        first_part_match = part in first_part_rules
        second_part_match = part in second_part_rules

        if not first_part_match and second_part_match:
            first_part = False

        if not first_part_match and not second_part_match:
            good = False

        if first_part:
            first_part_count += 1
        else:
            second_part_count += 1

        i += p_len

    if second_part_count >= first_part_count:
        good = False

    return good


first_part = '42'
second_part = '31'

first_part_combinations = set()
second_part_combinations = set()

for rule in generate_rules(rules, first_part):
    for n in rule.split('|'):
        first_part_combinations.add(n)

for rule in generate_rules(rules, second_part):
    for n in rule.split('|'):
        second_part_combinations.add(n)

print('Part One Solution: ', find_solution1(messages, first_part_combinations, second_part_combinations))
print('Part Two Solution: ', find_solution2(messages, first_part_combinations, second_part_combinations))
