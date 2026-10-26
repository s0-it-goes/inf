import random

n :int = int(input())
k :int = int(input())

a = []

for i in range(n):
    a.append(random.randint(-100, 100))
    print(a[i], end = " ")

print('\n')

shift = k % n

for i in range(shift):
    for j in range(n):
        if j == 0:
            tmp = a[j]
            a[j] = a[-1]
            continue

        tmp2 = a[j]
        a[j] = tmp
        tmp = tmp2

print('\n', a)