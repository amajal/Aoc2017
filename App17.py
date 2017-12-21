from collections import deque

def part_1():
    steps_per_insert = 324

    buffer = [0]
    repetitions = 2017
    current = 0

    for step in range(1, repetitions + 1):
        current = ((current + steps_per_insert) % len(buffer)) + 1
        buffer.insert(current, step)

    print(buffer[current-3], buffer[current-2], buffer[current-1], buffer[current], buffer[current+1], buffer[current+2], buffer[current+3])


def part_2_b():
    steps_per_insert = 324

    repetitions = 50000000
    current = 0
    output = 0

    for step in range(1, repetitions + 1):
        current = ((current + steps_per_insert) % step) + 1
        if current == 1:
            output = step

    print(output)



def part_2():
    steps_per_insert = 324

    buffer = deque([0])
    repetitions = 50000000

    for step in range(1, repetitions + 1):
        buffer.rotate(-steps_per_insert)
        buffer.append(step)

    print(buffer[(buffer.index(0) + 1) % len(buffer)])

part_1()
#part_2()
part_2_b()