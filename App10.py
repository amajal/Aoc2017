import math, functools

size = 256
hash_string = "63,144,180,149,1,255,167,84,125,65,188,0,2,254,229,24"
hash_array = []
num_array = []


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
        print(chunk)
        dense_array.append(functools.reduce(lambda x, y: x ^ y, chunk))

    print(dense_array)
    return dense_array

for num in range(0, size):
    num_array.append(num)


for s in hash_string:
    hash_array.append(ord(s))

hash_array += [17, 31, 73, 47, 23]

print(hash_array)

current = 0
skip_size = 0

for round in range(1, 65):
    for hash_index, length in enumerate(hash_array):
        #print(num_array, "Length %s, SkipSize %s, Current %s" %(length, skip_size, current))
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

print(hash_output)
