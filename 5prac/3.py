N :int = int(input())

cnt = 0
tmp = 0


for i in range(1, N):
    pow = len(str(i))
    for j in range(pow):
        tmp += int(str(i)[j]) ** pow

    if tmp == i:
        cnt += 1
        
    tmp = 0

print(cnt)