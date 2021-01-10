with open('puzzle_inputs.txt') as f:
    inputs = [line.replace('\n', '') for line in f]


def evaluate_expression(expression, start=0):
    i = start
    number = ''

    n = []

    while i < len(expression):
        c = expression[i]
        if c == '(':
            i, number = evaluate_expression(expression, i + 1)
            number = str(number)
        elif c == ')':
            n.append(int(number))
            i += 1
            break
        elif c in ['+', '*']:
            n.append(int(number))
            n.append(c)
            number = ''
        else:
            number += c
        i += 1
    n.append(int(number))

    value = int(n[0])

    j = 1
    while j < len(n) - 1:
        op = n[j]
        if op == '+':
            value += int(n[j + 1])
        else:
            value *= int(n[j + 1])
        j += 2

    return i - 1, value


def find_solution1(inputs):
    answers = []
    for input in inputs:
        _, value = evaluate_expression(input.replace(' ', ''))
        answers.append(value)
    return sum(answers)


print('Part one solution: ', find_solution1(inputs))
