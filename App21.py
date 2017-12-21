
import numpy as np
import datetime

rule_book = {}


def insert_transformed_string(new_image, transformed_grid, row_offset, column_offset):
    length = transformed_grid.shape[0]

    for c in range(0, length):
        for r in range(0, length):
            new_image[(r+row_offset), (c+column_offset)] = transformed_grid[r, c]


def count_switches(image):
    count = 0
    for c in range(0, image.shape[1]):
        for r in range(0, image.shape[0]):
            if image[r, c] == "#":
                count += 1

    return count


def generate_default_image():
    default_string = ".#...####"
    return np.array(",".join(default_string).split(","), np.str).reshape(3,3)


def convert_to_lookup_string(grid):
    grid_string = np.array2string(grid, grid.shape[0])[2:-2].replace("]", "/")
    look_up_string = ''.join([c for c in grid_string if c in ("/", "#", ".")])

    return look_up_string


def update_rule_book(lookup_strings, rule):
    for lookup_string in lookup_strings:
        if lookup_string not in rule_book.keys():
            rule_book[lookup_string] = rule


def transform(grid_to_transform):
    new_length = grid_to_transform.shape[0] + 1

    lookup_strings = []
    for rotate in (0, 1, 2, 3):
        rotated_grid = np.rot90(grid_to_transform, rotate)
        for flip in (rotated_grid, np.fliplr(rotated_grid), np.flipud(rotated_grid)):
            current_grid = flip
            lookup_strings.append(convert_to_lookup_string(current_grid))

            for lookup_string in lookup_strings:
                if lookup_string in rule_book.keys():
                    rule = rule_book[lookup_string]
                    update_rule_book(lookup_strings, rule)
                    transformed_string = rule.replace("/", "")
                    transformed_grid = np.array(",".join(transformed_string).split(",")).reshape(new_length, new_length)
                    return transformed_grid

    print("No lookup found")
    print(grid_to_transform)
    quit()


prog_start_time = datetime.datetime.now()

with open("Input.txt", "r") as f:
    rules = f.read().split('\n')

for rule in rules:
    tokens = rule.split("=>")
    rule_book[tokens[0].strip()] = tokens[1].strip()

image = generate_default_image()

for iterations in range(1, 19):

    start_time = datetime.datetime.now()

    dimension = image.shape[0]

    if dimension % 2 == 0:
        partition_length = 2
    elif dimension % 3 == 0:
        partition_length = 3

    partitions = int(dimension / partition_length)
    new_size = (partition_length + 1) * partitions
    new_image = np.empty((new_size, new_size), dtype=np.str)

    for column_partition in range(1, partitions + 1):
        for row_partition in range(1, partitions + 1):

                start_row_index = partition_length * (row_partition - 1)
                end_row_index = partition_length * row_partition
                start_col_index = partition_length * (column_partition - 1)
                end_col_index = partition_length * column_partition

                new_image_row_offset = (partition_length + 1) * (row_partition - 1)
                new_image_column_offset = (partition_length + 1) * (column_partition - 1)

                sub_grid = image[start_row_index:end_row_index, start_col_index:end_col_index]
                transformed_grid = transform(sub_grid)
                insert_transformed_string(new_image, transformed_grid, new_image_row_offset, new_image_column_offset)

    image = new_image
    print("Iteration:", iterations, (datetime.datetime.now() - prog_start_time))

print("On Switches: ", count_switches(image), datetime.datetime.now() - prog_start_time)