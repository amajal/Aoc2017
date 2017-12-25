import time, functools
import collections

start_time = time.clock()


def sum_bridge(bridge):
    sum = 0
    for component in bridge:
        sum += int(component[0]) + int(component[1])

    return sum


def max_length_bridge(bridges):
    max_length = 0
    max_sum = 0
    for bridge in bridges:
        bridge_length = len(bridge)

        if bridge_length > max_length:
            max_sum = 0
            max_length = bridge_length

        if bridge_length == max_length:
            sum = sum_bridge(bridge)
            if sum > max_sum:
                max_sum = sum

    return max_sum



def build_bridges():
    bridges = collections.deque()
    zero_pin_connectors = get_components_with_leading_pins("0")
    queue = collections.deque()
    for connector in zero_pin_connectors:
        queue.append(connector)

    while len(queue) > 0:
        current_bridge = queue.popleft()
        bridges.append(current_bridge)
        last_link_pin = current_bridge[-1][1]

        for component in initial_components:
            if component[0] in current_bridge or component[1] in current_bridge:
                continue

            for i in (0, 1):
                if last_link_pin == component[i][0]:
                    new_bridge = current_bridge.copy()
                    new_bridge.append(component[i])
                    queue.append(new_bridge)

        #print(time.clock() - start_time, len(queue))

    return bridges


def get_components_with_leading_pins(pins_to_match):
    matching_components = collections.deque()

    for component in initial_components:
        for i in (0,1):
            if pins_to_match == component[i][0]:
                matching_components.append([(component[i])])

    return matching_components


initial_components = collections.deque()

with open("Input.txt", "r") as f:
    components = f.read().split('\n')
    for component in components:
        tokens = component.split('/')
        reverse_tokens = tokens.copy()
        reverse_tokens.reverse()
        initial_components.append((tokens, reverse_tokens))

print(initial_components)

bridges = build_bridges()

print("Bridge generation finished", time.clock() - start_time)
#for bridge in bridges:
#    print(bridge)
max_sum = max(map(sum_bridge, bridges))
print("Max sum eval finished", max_sum, time.clock() - start_time)
max_length_sum = max_length_bridge(bridges)
print("Max length sum eval finished", max_length_sum, time.clock() - start_time)
