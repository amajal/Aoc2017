
inputFile = "Input2.txt"

testInput = open(inputFile, 'r').readlines()

for line in testInput:
    line = line.rstrip()
    length_of_list = len(line)

    print(line)
    next = 0
    sum = 0

    for i, s in enumerate(line):
        next = int((i + (length_of_list / 2)) % length_of_list)

        print(i, next)

        if s == line[next]:
            sum = sum + int(s)

    print(sum)
