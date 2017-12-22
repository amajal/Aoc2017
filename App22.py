import numpy as np
import math


def find_mid_point(cluster):
    mid_x = int(math.ceil(cluster.shape[0] / 2)) - 1
    mid_y = int(math.ceil(cluster.shape[1] / 2)) - 1
    return mid_x, mid_y


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


for burst in range (1, 8):
    current_node = cluster[current_x, current_y]
    print_cluster = cluster.copy()
    print_cluster[current_x, current_y] = "_"
    print(print_cluster)
    print(current_x, current_y, direction, current_node)

    direction = rotate(current_node, direction)


    if current_node == '#':
        cluster[current_x, current_y] = 'c'
    elif current_node == '.':
        cluster[current_x, current_y] = '#'

    current_x, current_y = move_forward(direction, current_x, current_y)

    print(current_x, current_y, direction)

    if current_x == -1:
        cluster = np.insert(cluster, 0, '.', axis=0)
        current_x = 0

    if current_x == cluster.shape[0]:
        cluster = np.insert(cluster, cluster.shape[0], '.', axis=0)

    if current_y == -1:
        cluster = np.insert(cluster, 0, '.', axis=1)
        current_y = 0

    if current_y == cluster.shape[1]:
        cluster = np.insert(cluster, cluster.shape[1], '.', axis=1)


