from string import ascii_lowercase

with open('puzzle_inputs.txt') as f:
    inputs = [line.replace('\n', '') for line in f]


def parse_forms(inputs):
    forms = []
    form = {letter: False for letter in ascii_lowercase}

    for input in inputs:
        if len(input) == 0:
            forms.append(form)
            form = {letter: False for letter in ascii_lowercase}
        else:
            for letter in input:
                form[letter] = True
    forms.append(form)
    return forms


forms = parse_forms(inputs)


def find_solution1(forms):
    count = 0

    for form in forms:
        for letter in form:
            count += 1 if form[letter] is True else False
    return count


print("Part one solution: ", find_solution1(forms))
