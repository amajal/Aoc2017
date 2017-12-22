import numpy as np
import math, time


def find_mid_point(length):
    return int(math.ceil(length / 2)) - 1


def rotate(node, direction):
    rotation = dict()
    rotation["up"] = ("right", "left", "down")
    rotation["right"] = ("down", "up", "left")
    rotation["down"] = ("left", "right", "up")
    rotation["left"] = ("up", "down", "right")

    index = 1
    if node == '#':
        index = 0

    if node == 'F':
        index = 2

    return rotation[direction][index]


def move_forward(direction, row_index, column_index):
    if direction == "right":
        column_index += 1

    if direction == "left":
        column_index -= 1

    if direction == "up":
        row_index -= 1

    if direction == "down":
        row_index += 1

    return row_index, column_index


start_time = time.clock()

with open("Input.txt", "r") as f:
    puzzle_input = f.read()

rows = puzzle_input.count("\n") + 1
puzzle_input = puzzle_input.replace("\n", "")
columns = int(len(puzzle_input) / rows)

cluster = np.array(list(puzzle_input), dtype=np.str).reshape(rows, columns)


row_index = find_mid_point(cluster.shape[0])
column_index = find_mid_point(cluster.shape[1])
direction = "up"
counter = 0

for burst in range(1, 10000000+1):
    current_node = cluster[row_index, column_index]

    if current_node == '#':
        direction = rotate(current_node, direction)
        cluster[row_index, column_index] = 'F'
    elif current_node == '.':
        direction = rotate(current_node, direction)
        cluster[row_index, column_index] = 'W'
    elif current_node == 'W':
        cluster[row_index, column_index] = '#'
        counter += 1
    elif current_node == 'F':
        direction = rotate(current_node, direction)
        cluster[row_index, column_index] = '.'

    row_index, column_index = move_forward(direction, row_index, column_index)

    if row_index == -1:
        cluster = np.insert(cluster, 0, '.', axis=0)
        row_index = 0

    if row_index == cluster.shape[0]:
        cluster = np.insert(cluster, cluster.shape[0], '.', axis=0)

    if column_index == -1:
        cluster = np.insert(cluster, 0, '.', axis=1)
        column_index = 0

    if column_index == cluster.shape[1]:
        cluster = np.insert(cluster, cluster.shape[1], '.', axis=1)

    if burst % 100000 == 0:
        print("Burst: ", burst, time.clock() - start_time)

    #print_cluster = cluster.copy()
    #print_cluster[row_index, column_index] = "_"
    #print("Burst: ", burst, row_index, column_index, direction, current_node)
    #print(cluster)
    #print(print_cluster)

print(counter)

