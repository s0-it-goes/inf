n :int = int(input())
k :int = int(input())

a :list = []

for i in range(n):
    a.append(i+1)
    print(a[i], end = " ")

print('\n')

cnt :int = 0
i :int = 0

while(len(a) != 1):
    cnt += 1
    if cnt == k:
        print(a[i], end = ' ')
        a.pop(i)
        cnt = 0
    else:
        i+= 1
    if i == len(a):
        i = 0

print('/', a[0])