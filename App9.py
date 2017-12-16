

def process_stream(stream):
    score = 0
    level = 0
    garbage_counter = 0

    while len(stream) > 0:
        current = stream.pop(0)

        if current == "<":
            current = stream.pop(0)

            while current != ">":
                if current == "!":
                    stream.pop(0)
                else:
                    garbage_counter += 1

                current = stream.pop(0)

        if current == "{":
            level += 1

        if current == "}":
            score += level
            level -= 1

    return garbage_counter


with open("Input1.txt") as f:
    data = f.readlines()
    for stream in data:
        print(stream.rstrip("\n"), process_stream(list(stream)))
