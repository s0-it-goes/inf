import sys

n = int(input())

if n <= 2:
    sys.exit()
    
def make_magic_square(N):
    square = [[0] * N for i in range(N)]

    position = [0, N // 2]
    cnt = 0

    number = 0

    for i in range(N):
        for j in range(N):
            number += 1

            if cnt == N:
                position[0] += 2
                position[1] -= 1
                cnt = 0
            if position[1] >= N:
                position[1] = 0
            if position[0] < 0:
                position[0] = N-1

            square[position[0]][position[1]] = number

            position[0] -= 1
            position[1] += 1
            
            cnt += 1       

    return square

x = make_magic_square(n)

for i in range(n):
    print(x[i])