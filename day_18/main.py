with open('puzzle_inputs.txt') as f:
    inputs = [line.replace('\n', '') for line in f]


def evaluate_stack(stack, advanced=False):
    if advanced:
        j = 1
        while j < len(stack) - 1:
            op = stack[j]

            if op == '+':
                stack[j] = int(stack[j - 1]) + int(stack[j + 1])
                del stack[j - 1]
                del stack[j]
                continue

            j += 2

    value = int(stack[0])
    j = 1
    while j < len(stack) - 1:
        op = stack[j]
        if op == '+':
            value += int(stack[j + 1])
        else:
            value *= int(stack[j + 1])
        j += 2

    return value


def evaluate_expression(expression, start=0, advanced=False):
    i = start
    number = ''

    stack = []

    while i < len(expression):
        c = expression[i]
        if c == '(':
            i, number = evaluate_expression(expression, i + 1, advanced)
            number = str(number)
        elif c == ')':
            stack.append(int(number))
            i += 1
            break
        elif c in ['+', '*']:
            stack.append(int(number))
            stack.append(c)
            number = ''
        else:
            number += c
        i += 1
    stack.append(int(number))

    return i - 1, evaluate_stack(stack, advanced=advanced)


def find_solution1(inputs):
    answers = []
    for input in inputs:
        _, value = evaluate_expression(input.replace(' ', ''))
        answers.append(value)
    return sum(answers)


def find_solution2(inputs):
    answers = []
    for input in inputs:
        _, value = evaluate_expression(input.replace(' ', ''), advanced=True)
        answers.append(value)
    return sum(answers)


print('Part one solution: ', find_solution1(inputs))

print('Part two solution: ', find_solution2(inputs))
