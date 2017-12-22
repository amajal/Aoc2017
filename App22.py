import numpy as np
import math

def find_mid_point(cluster):
    mid_x = cluster.shape[0] / 2


with open("Input.txt", "r") as f:
    puzzle_input = f.read()

height = puzzle_input.count("\n") + 1
puzzle_input = puzzle_input.replace("\n", "")
width = int(len(puzzle_input) / height)

print(width, height)

cluster = np.array(list(puzzle_input), dtype=np.str).reshape(width, height)


current_x, current_y = find_mid_point(cluster)


print(cluster)
print(current_x, current_y)