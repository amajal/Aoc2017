import math

input = 277678
max = 9
width = 1
counter, current = 1, 1
x, y = 0, 0
direction = "right"
value_map = {(0,0):1}


def distance_from_origin(x, y):
    return math.fabs(x) + math.fabs(y)


def next_coordinate(x, y, direction):
    if direction == "up":
        return x, y + 1

    if direction == "left":
        return x - 1, y

    if direction == "right":
        return x + 1, y

    if direction == "down":
        return x, y - 1


def get_current_direction(x, y, prev_direction):

    if direction == 'right' and x == width:
        return 'up'

    if direction == 'up' and y == width:
        return 'left'

    if direction == 'left' and x == width * -1:
        return 'down'

    if direction == 'down' and y == width * -1:
        return 'right'

    return prev_direction


def get_computed_val(x, y):
    sum = 0

    # Right
    sum = sum + get_val(x + 1, y)

    # Top Right
    sum = sum + get_val(x + 1, y + 1)

    # Top
    sum = sum + get_val(x, y + 1)

    # Top Left
    sum = sum + get_val(x - 1, y + 1)

    # Left
    sum = sum + get_val(x - 1, y)

    # Bottom Left
    sum = sum + get_val(x - 1, y - 1)

    # Bottom
    sum = sum + get_val(x, y - 1)

    # Bottom Right
    sum = sum + get_val(x + 1, y - 1)

    print (x,y,sum)

    return sum


def get_val(x, y):
    if (x, y) in value_map:
        return value_map[(x,y)]
    else:
        return 0


while current < input:
    counter = counter + 1

    if counter == max:
        max = (math.sqrt(max) + 2) ** 2
        width = width + 1

    direction = get_current_direction(x, y, direction)
    x, y = next_coordinate(x, y, direction)
    current = get_computed_val(x, y)
    value_map[(x, y)] = current
    #print(x, y, width, current, direction)


print(current)

