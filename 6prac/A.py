import random

lottery = [random.randint(1, 49) for i in range(6)]

print(*lottery)