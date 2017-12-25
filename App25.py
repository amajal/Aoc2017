import collections, time

start_time = time.clock()

with open("Input.txt", "r") as f:
    input = f.readlines()

current_state = input[0][-3]
steps = int(input[1].split()[-2])

state_instructions = input[2:]
number_of_states = int(len(state_instructions) / 10)

states = dict()

for i in range(0, number_of_states):
    offset = i * 10
    state_name = state_instructions[offset + 1][-3]
    state_behavior = dict()
    for condition in (0, 1):
        inner_offset = (offset + 2) + (condition * 4)
        current_value = int(state_instructions[inner_offset][-3])
        new_value = int(state_instructions[inner_offset + 1][-3])
        direction = state_instructions[inner_offset + 2]
        next_state = state_instructions[inner_offset + 3].split(" ")[-1][0]

        increment = 0
        if "right" in direction:
            increment = 1
        elif "left" in direction:
            increment = -1
        state_behavior[current_value] = (new_value, increment, next_state)

    states[state_name] = state_behavior


tape = collections.deque()
tape.append(0)
current_index = 0

print(states)

for step in range(1, steps + 1):
    behavior = states[current_state][tape[current_index]]
    tape[current_index] = behavior[0]
    current_index += behavior[1]

    if current_index == len(tape):
        tape.append(0)

    if current_index < 0:
        tape.appendleft(0)
        current_index = 0

    current_state = behavior[2]


print(tape.count(1), time.clock() - start_time)