import numpy as np
import math


def find_mid_point(cluster):
    mid_x = int(math.ceil(cluster.shape[0] / 2)) - 1
    mid_y = int(math.ceil(cluster.shape[1] / 2)) - 1
    return mid_x, mid_y


def extend_columns(val):
    number_of_rows = cluster.shape[0]
    number_of_columns = cluster.shape[1]

    splits = np.hsplit(cluster, number_of_columns)
    new_array = np.array(list("." * number_of_rows), dtype=np.str).reshape(number_of_rows, 1)

    if val == -1:
        splits.insert(new_array, 0)
    else:
        splits.append(new_array)

    return np.hstack(splits)


def extend_rows(val):
    number_of_rows = cluster.shape[0]
    number_of_columns = cluster.shape[1]

    splits = np.vsplit(cluster, number_of_rows)
    new_array = np.array(list("." * number_of_columns)).reshape(number_of_columns, 1)

    if val == -1:
        splits.insert(new_array, 0)
    else:
        splits.append(new_array)

    return np.vstack(splits)


def resize_cluster(x, y, cluster):
    num_of_rows = cluster.shape[0]
    num_of_columns = cluster.shape[1]

    print("Resize:",  x, y)

    if x in (-1, num_of_columns):
        return extend_columns(x)
    elif y in (-1, num_of_rows):
        return extend_rows(y)
    else:
        return cluster


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


def move_forward(direction, x, y):
    if direction == "right":
        x += 1

    if direction == "left":
        x -= 1

    if direction == "up":
        y -= 1

    if direction == "down":
        y += 1

    return x, y


with open("Input.txt", "r") as f:
    puzzle_input = f.read()

height = puzzle_input.count("\n") + 1
puzzle_input = puzzle_input.replace("\n", "")
width = int(len(puzzle_input) / height)

cluster = np.array(list(puzzle_input), dtype=np.str).reshape(width, height)
current_x, current_y = find_mid_point(cluster)
direction = "up"

print(cluster)

for burst in range (1, 6):
    current_node = cluster[current_x, current_y]
    print(current_x, current_y, current_node)

    direction = rotate(current_node, direction)

    if current_node == '#':
        cluster[current_x, current_y] = 'c'
    elif current_node == '.':
        cluster[current_x, current_y] = '#'

    current_x, current_y = move_forward(direction, current_x, current_y)

    cluster = resize_cluster(current_x, current_y, cluster)

    print(cluster)