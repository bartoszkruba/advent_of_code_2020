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


def x(str, rules):
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
    arr = [rules['0']]
    while True:
        new_arr = []
        for s1 in arr:
            for s2 in x(s1, rules):
                new_arr.append(s2)
        if arr == new_arr:
            break
        arr = new_arr

    for i in range(len(arr)):
        arr[i] = arr[i].replace('"', '').replace(' ', '')

    count = 0

    for message in messages:
        if message in arr:
            count += 1

    return count
