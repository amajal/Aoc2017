

def get_last_sixteen_bits(num):
    return str(bin(num))[-16:]


seed_A = 783
seed_B = 325
factor_A = 16807
factor_B = 48271
divisor = 2147483647

values_A = []
values_B = []

while min(len(values_A), len(values_B)) < 5000000:
    next_A = (seed_A * factor_A) % divisor
    next_B = (seed_B * factor_B) % divisor

    if next_A % 4 == 0:
        values_A.append(next_A)

    if next_B % 8 == 0:
        values_B.append(next_B)

    seed_A = next_A
    seed_B = next_B

sum = 0
for i in range(0, 5000000):
    if get_last_sixteen_bits(values_A[i]) == get_last_sixteen_bits(values_B[i]):
        sum += 1


print(sum)