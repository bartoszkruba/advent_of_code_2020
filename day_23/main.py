with open('puzzle_inputs.txt') as f:
    for line in f:
        line = line.replace('\n', '')
        bucket = [int(number) for number in line]


def get_pick_up(current_cup, bucket):
    indx = bucket.index(current_cup)
    if indx + 4 < len(bucket):
        pick_up = bucket[indx + 1: indx + 4]
    elif indx == len(bucket) - 1:
        pick_up = bucket[0: 3]
    else:
        pick_up = bucket[indx + 1: indx + 4] + bucket[0: indx + 4 - len(bucket)]
    return pick_up


def get_destination(current_cup, pick_up):
    destination = current_cup - 1

    while True:
        if destination < 1:
            destination = 9

        if destination not in pick_up and destination != current_cup:
            return destination
        else:
            destination -= 1


def format_answer(bucket):
    answer = ''
    i = bucket.index(1) + 1

    while len(answer) < 8:
        if i >= len(bucket):
            i = 0

        answer += str(bucket[i])

        i += 1

    return answer


def find_solution1(bucket):
    current_cup = bucket[0]
    for i in range(100):

        pick_up = get_pick_up(current_cup, bucket)
        destination = get_destination(current_cup, pick_up)

        for number in pick_up:
            bucket.remove(number)

        indx = bucket.index(destination)

        for j in range(3):
            bucket.insert(indx + 1, pick_up[2 - j])

        indx = bucket.index(current_cup) + 1
        if indx == len(bucket):
            indx = 0

        current_cup = bucket[indx]

    return format_answer(bucket)


print('Part One Solution: ', find_solution1(bucket))
