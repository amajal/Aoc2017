
file_name = 'Input1.txt'
data = open(file_name, 'r').readlines()
sum = 0
for line in data:
    tokens = list(map(int, line.split()))

    for i, divisor in enumerate(tokens):
        for j, dividend in enumerate(tokens):
            if i == j:
                continue

            if divisor % dividend == 0:
                sum = sum + (divisor / dividend)

print(sum)