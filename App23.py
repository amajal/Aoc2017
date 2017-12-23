import time


def create_program():
    registers = {}

    for letter in range(97, 105):
        registers[chr(letter)] = 0

    return {'registers': registers}


def convert_to_val (token, registers):
    if token.startswith('-') or token.isdigit():
        return int(token)
    else:
        return registers[token]


def execute_program(program):
    start_time = time.clock()

    registers = program['registers']
    registers['a'] = 1
    counter = 0
    run_count = 0

    while counter < len(instructions):
        tokens = instructions[counter].split()
        cmd = tokens[0]
        val = convert_to_val(tokens[1], registers)
        instruction_register = tokens[1]

        if len(tokens) == 3:
            op3 = convert_to_val(tokens[2], registers)

        if cmd in 'set':
            registers[instruction_register] = op3
        elif cmd in "sub":
            registers[instruction_register] -= op3
        elif cmd in "mul":
            registers[instruction_register] *= op3

        if cmd in "jnz" and val != 0:
            if op3 < 0:
                counter += op3 - 1

        counter += 1
        run_count += 1

        if run_count % 1000000 == 0:
            print(run_count, time.clock() - start_time)
            print(registers)

    return registers['h']


def parse_program(instructions):
    output = []
    for i, instruction in enumerate(instructions):
        tokens = instructions[i].split()
        cmd = tokens[0]

        if cmd in 'set':
            output.append(tokens[1] + " = " + tokens[2])
        elif cmd in "sub":
            output.append(tokens[1] + " = " + tokens[1] + " - " + tokens[2])
        elif cmd in "mul":
            output.append(tokens[1] + " = " + tokens[1] + " * " + tokens[2])

        if cmd in "jnz":
            offset = int(tokens[2])

            #if (offset > 0)
            output.append("if " + tokens[1] + " !=  0; jump " + str(offset))

    print("\n".join(output))
    quit()

    return output


with open("Input2.txt") as f:
    instructions = f.readlines()

program = create_program()
#parse_program(instructions)
value = execute_program(program)
print(value)
