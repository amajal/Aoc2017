
import numpy as np
import datetime, math

initial_string = ".#...####"


def insert_transformed_string(new_image, transformed_grid, row_offset, column_offset):
    length = transformed_grid.shape[0]
    for c in range(0, length):
        for r in range(0, length):
            new_image[(r+row_offset), (c+column_offset)] = transformed_grid[r, c]


def generate_rule_book():
    rule_book = {}

    with open("Input.txt", "r") as f:
        rules = f.read().split('\n')

    for rule in rules:
        tokens = rule.split("=>")
        input_image = tokens[0].strip()
        output_image = tokens[1].strip()

        input_image_variations = generate_rule_variations(input_image)

        for input_image_variation in input_image_variations:
            rule_book[input_image_variation] = output_image

    return rule_book


def generate_rule_variations(image):
    image_variations = []
    image_grid = convert_string_to_array(image.replace("/", ""))

    for rotate in (0, 1, 2, 3):
        rotated_grid = np.rot90(image_grid, rotate)
        flipped_grid = np.fliplr(rotated_grid)
        image_variations.append(convert_array_to_string(rotated_grid))
        image_variations.append(convert_array_to_string(flipped_grid))

    return image_variations


def count_switches(grid):
    count = 0
    for c in range(0, grid.shape[1]):
        for r in range(0, grid.shape[0]):
            if grid[r, c] == "#":
                count += 1
    return count


def convert_string_to_array(image):
    dimension = int(math.sqrt(len(image)))
    return np.array(",".join(image).split(","), np.str).reshape(dimension, dimension)


def convert_array_to_string(grid):
    grid_string = np.array2string(grid, grid.shape[0])[2:-2].replace("]", "/")
    look_up_string = ''.join([c for c in grid_string if c in ("/", "#", ".")])
    return look_up_string


prog_start_time = datetime.datetime.now()
rule_book = generate_rule_book()
image = convert_string_to_array(initial_string)

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
                sub_grid_string = convert_array_to_string(sub_grid)
                transformed_image_string = rule_book[sub_grid_string].replace("/", "")
                transformed_image_grid = convert_string_to_array(transformed_image_string)
                insert_transformed_string(new_image, transformed_image_grid, new_image_row_offset, new_image_column_offset)

    image = new_image
    print("Iteration:", iterations, np.count_nonzero(image == '#'), (datetime.datetime.now() - prog_start_time))