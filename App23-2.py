import time, math


def is_prime(n):
    limit = int(math.sqrt(n)) + 1

    if n % 2 == 0:
        return False

    for i in range(2, limit + 1):
        if n % i == 0:
            return False

    return True


b = 108400
c = 125400

print((c - b) / 17)

h = 0
start_time = time.clock()

for n in range(b, c+1, 17):
    if is_prime(n) is False:
        h += 1

print(h, time.clock() - start_time)
