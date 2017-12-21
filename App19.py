from functools import reduce

stations = []
junction = "+"


def current(x, y):
    return route[y][x]


def step(x, y, direction):
    if direction is "Up":
        y += -1
    elif direction is "Down":
        y += 1
    elif direction is "Right":
        x += 1
    elif direction is "Left":
        x -= 1

    return x, y


def is_a_station(x, y):
    current = str(route[y][x])
    if 65 <= ord(current) <= 90:
        return True
    else:
        return False


def get_next_direction(x, y, old_direction, route):
    vertical_directions = ["Up", "Down"]
    horizontal_directions = ["Left", "Right"]

    if old_direction in vertical_directions:
        possible_directions = horizontal_directions
    else:
        possible_directions = vertical_directions

    for direction in possible_directions:
            local_x, local_y = step(x, y, direction)
            print(local_x, local_y)
            if 0 <= local_y < len(route) and 0 <= local_x < len(route[local_y]) and route[local_y][local_x] not in '.':
                return direction

    return ""


with open("Test.txt", "r") as f:
    input = f.read().replace(' ', '.').split('\n')
    route = list(map(lambda x: list(str(x).replace(" ", ".")), input))


y = 0
x = route[0].index('|')
direction = "Down"
counter = 0

while True:
    if current(x, y) == '.':
        break

    if is_a_station(x, y):
        stations.append(current(x, y))

    if current(x, y) == '+':
        direction = get_next_direction(x, y, direction, route)

        if direction == "":
            break

    x, y = step(x, y, direction)
    counter += 1


print("".join(stations))
print(counter)