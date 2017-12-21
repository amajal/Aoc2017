

def get_counters(programs):
    return list(map(lambda x: x['counter'], programs))


def create_program (id):
    registers = {}

    for letter in range(97, 123):
        registers[chr(letter)] = 0

    registers['p'] = id

    return {'registers': registers, 'queue': [], 'counter': 0, 'processid': id}


def convert_to_val (token, registers):
    if token.startswith('-') or token.isdigit():
        return int(token)
    else:
        return registers[token]


def execute_program(program, read_queue):
    registers = program['registers']
    counter = program['counter']
    write_queue = program['queue']
    process_id = program['processid']
    global my_global_counter

    while counter < len(instructions):
        tokens = instructions[counter].split()
        cmd = tokens[0]
        val = convert_to_val(tokens[1], registers)
        instruction_register = tokens[1]

        if len(tokens) == 3:
            op3 = convert_to_val(tokens[2], registers)

        if cmd in "snd":
            write_queue.append(val)
            if process_id == 1:
                my_global_counter += 1
        elif cmd in 'set':
            registers[instruction_register] = op3
        elif cmd in "add":
            registers[instruction_register] += op3
        elif cmd in "mul":
            registers[instruction_register] *= op3
        elif cmd in "mod":
            registers[instruction_register] = registers[instruction_register] % op3
        elif cmd in "rcv":
            if len(read_queue) == 0:
                program['counter'] = counter
                return
            else:
                registers[instruction_register] = int(read_queue.pop(0))

        if cmd in "jgz" and val > 0:
                counter += op3 - 1

        counter += 1



with open("Input.txt") as f:
    instructions = f.readlines()

my_global_counter = 0

programs = [create_program(0), create_program(1)]

while True:
    pre_counters = get_counters(programs)

    for program in range(0, 2):
        read_queue = programs[(program + 1) % 2]['queue']
        execute_program(programs[program], read_queue)

    post_counters = get_counters(programs)

    print(pre_counters, post_counters)
    if len(programs[0]['queue']) == 0 and len(programs[1]['queue']) == 0:
        print("Deadlock detected ... terminating")
        print(my_global_counter)
        quit()
