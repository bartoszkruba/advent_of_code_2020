from string import ascii_lowercase

with open('puzzle_inputs.txt') as f:
    inputs = [line.replace('\n', '') for line in f]


def parse_forms(inputs):
    forms = []
    form = {letter: 0 for letter in ascii_lowercase}
    form['total'] = 0

    for input in inputs:
        if len(input) == 0:
            forms.append(form)
            form = {letter: 0 for letter in ascii_lowercase}
            form['total'] = 0
        else:
            form['total'] += 1
            for letter in input:
                form[letter] += 1
    forms.append(form)
    return forms


forms = parse_forms(inputs)


def find_solution1(forms):
    count = 0

    for form in forms:
        for letter in ascii_lowercase:
            count += 1 if form[letter] > 0 else 0
    return count


print("Part one solution: ", find_solution1(forms))


def find_solution2(forms):
    count = 0

    for form in forms:
        for letter in ascii_lowercase:
            count += 1 if form[letter] == form['total'] else 0
    return count


print("Part two solution: ", find_solution2(forms))
