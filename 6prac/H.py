n = int(input())

current = []
max = []

print("Введите сколько человек в комнате и вместительность")
while n > 0:
    current.append(int(input()))
    max.append(int(input()))
    n -= 1

cnt = 0

for i in range(len(current)):
    if max[i] - current[i] >= 2:
        cnt += 1

print(f"Всего комнат поместят 2 человека: {cnt}")