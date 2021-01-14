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


def find_solution1(rules, messages):
    s = {rules['0']}
    while True:
        count = 0
        new_s = set()
        for s1 in s:
            for s2 in replace_rules(s1, rules):
                count += 1
                new_s.add(s2)
        if s == new_s:
            break
        s = new_s

    arr = []
    for i in s:
        arr.append(i.replace('"', '').replace(' ', ''))

    filtered_messages = []

    for message in messages:
        if message in arr:
            filtered_messages.append(message)

    return len(filtered_messages), filtered_messages


def x(rules, rule_start):
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


# answer, filtered_messages = find_solution1(rules, messages)
# print('Part One Solution:', answer)

# rules['8'] = '42 | 42 8'
# rules['11'] = '42 31 | 42 11 31'

# rule 0 = 8, 11 = x1 * 42, x2 * 42 + x2 * 31

rule_42_combinations = set()
rule_31_combinations = set()

for rule in x(rules, '42'):
    for n in rule.split('|'):
        rule_42_combinations.add(n)

for rule in x(rules, '31'):
    for n in rule.split('|'):
        rule_31_combinations.add(n)


def good_message(message, rules_42, rules_31):
    p_len = len(list(rule_42_combinations)[0])
    min_len = 3 * p_len

    good = True

    if len(message) < min_len or len(message) % p_len != 0:
        good = False
    elif message[-p_len:] not in rules_31:
        good = False
    elif message[0:p_len] not in rules_42 or message[p_len: 2 * p_len] not in rules_42:
        good = False

    i = 0
    first_part = True
    first_part_count = 0
    second_part_count = 0
    while i <= len(message) - p_len:
        part = message[i: i + p_len]
        first_part_match = part in rules_42
        second_part_match = part in rules_31

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


def good_message2(message, rules_42, rules_31):
    p_len = len(list(rule_42_combinations)[0])

    if len(message) != 3 * p_len:
        return False

    start = message[:p_len]
    middle = message[p_len: 2 * p_len]
    end = message[2 * p_len: 3 * p_len]

    return start in rules_42 and middle in rules_42 and end in rules_31


counter = 0
for message in messages:
    if good_message(message, rule_42_combinations, rule_31_combinations): counter += 1

print(counter)
