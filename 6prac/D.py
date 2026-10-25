import random

coin = ['О', 'Р']

attempts = 0
cnt = 1
prev = -1

while cnt != 3:
    current = random.randint(0, 1)
    if current == prev:
        cnt += 1
    else:
        cnt = 1

    prev = current
    print(coin[current], end = " ")

    attempts += 1

print(f"(попыток:{attempts})") # f-строка