import math, functools, binascii

size = 256
hash_string = "ffayrhll"
disk = []


def reverse(num_list, start, length):
    mid = int(math.floor(length/2))
    for index in range(0, mid):
        from_index = int((start + index) % len(num_list))
        to_index = int((start + length - 1 - index) % len(num_list))

        temp = num_list[from_index]
        num_list[from_index] = num_list[to_index]
        num_list[to_index] = temp


def sparse_reduction(num_array):
    dense_array = []
    chunk_size = 16
    for chunk_num in range(0, int(len(num_array)/chunk_size)):
        chunk = num_array[chunk_num * chunk_size:(chunk_num + 1) * chunk_size]
        dense_array.append(functools.reduce(lambda x, y: x ^ y, chunk))

    return dense_array


def convert_hex_to_binary_string(hex_string):
    return ''.join('{0:04b}'.format(int(h, 16), 'b') for h in hex_string)


def mark_group(r, c, group, disk):
    points = []
    points.append((r, c))

    while len(points) > 0:
        current = points.pop(0)
        current_row = current[0]
        current_column = current[1]
        print("marking at", current_row, current_column)

        if len(disk) > current_row >= 0 and len(disk[0]) > current_column >= 0:
            if disk[current_row][current_column] == '#':
                disk[current_row][current_column] = str(group)

                points.append((current_row + 1, current_column))
                points.append((current_row - 1, current_column))
                points.append((current_row, current_column + 1))
                points.append((current_row, current_column - 1))


sum = 0
for row in range(0, 128):
    hash_array = []
    num_array = []

    hash_knot = hash_string + "-" + str(row)

    for num in range(0, size):
        num_array.append(num)

    for s in hash_knot:
        hash_array.append(ord(s))

    hash_array += [17, 31, 73, 47, 23]

    current = 0
    skip_size = 0

    for round in range(1, 65):
        for hash_index, length in enumerate(hash_array):
            reverse(num_array, current, length)
            current += (length + skip_size) % size
            skip_size += 1

    dense_array = sparse_reduction(num_array)
    hash_output = ""

    for item in dense_array:
        hex_code = hex(item)[2:]
        if len(hex_code) == 1:
            hex_code = "0"+hex_code
        hash_output += hex_code

    binary_string = convert_hex_to_binary_string(hash_output).replace('1', '#').replace('0', '.')
    disk.append(list(binary_string))
    sum += binary_string.count('#')

group = 0
for r in range(0, 128):
    for c in range(0, 128):
        current = disk[r][c]
        if current == '#':
            print("marking group " + str(group))
            #current = str(group)
            mark_group(r, c, group, disk)
            group += 1


print(disk)
print(sum)
print(group)