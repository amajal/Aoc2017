import numpy as np
import math


def find_mid_point(length):
    return int(math.ceil(length / 2)) - 1


def rotate(node, direction):
    rotation = dict()
    rotation["up"] = ("right", "left")
    rotation["right"] = ("down", "up")
    rotation["down"] = ("left", "right")
    rotation["left"] = ("up", "down")

    index = 1
    if node == '#':
        index = 0

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

for burst in range(1, 10000+1):
    current_node = cluster[row_index, column_index]
    direction = rotate(current_node, direction)

    if current_node == '#':
        cluster[row_index, column_index] = '.'
    elif current_node == '.':
        cluster[row_index, column_index] = '#'
        counter += 1

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


    print_cluster = cluster.copy()
    print_cluster[row_index, column_index] = "_"

    print("Burst: ", burst, row_index, column_index, direction, current_node)
    #print(cluster)
    print()
    #print(print_cluster)
    print()

print(counter)

