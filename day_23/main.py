with open('puzzle_inputs.txt') as f:
    for line in f:
        line = line.replace('\n', '')
        bucket = [int(number) for number in line]


def get_destination(current_cup, pick_up, highest_value):
    destination = current_cup - 1

    while True:
        if destination < 1:
            destination = highest_value

        if destination not in pick_up and destination != current_cup:
            return destination
        else:
            destination -= 1


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def simulate(cups, rounds):
    nodes = {}

    current_node = None
    first_node = None
    highest_value = 0

    for number in cups:
        if number > highest_value:
            highest_value = number

        node = Node(number)

        if current_node is None:
            current_node = node
            first_node = current_node
        else:
            current_node.next = node
            current_node = node

        nodes[number] = node

    current_node.next = first_node
    current_node = first_node

    for _ in range(rounds):
        next_node = current_node.next
        pick_up = [next_node.value, next_node.next.value, next_node.next.next.value]

        destination = nodes[get_destination(current_node.value, pick_up, highest_value)]

        current_node.next = next_node.next.next.next
        next_node.next.next.next = destination.next
        destination.next = next_node

        current_node = current_node.next

    return nodes


def find_solution1(bucket):
    nodes = simulate([number for number in bucket], 100)

    answer = ''
    node = nodes[1].next

    for _ in range(8):
        answer += str(node.value)
        node = node.next
    return answer


def find_solution2(bucket):
    nodes = simulate([number for number in bucket] + list(range(10, 1_000_001)), 10_000_000)

    answer = 1
    node = nodes[1]

    for _ in range(3):
        answer *= node.value
        node = node.next

    return answer


print('Part One Solution: ', find_solution1([number for number in bucket]))
print('Part Two Solution: ', find_solution2([number for number in bucket]))
