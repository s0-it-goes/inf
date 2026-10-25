import random

rand  :int = random.randint(1, 100)
guess :int = 0

while(rand != guess):
    guess = int(input())
    print("Больше" if rand > guess else "Меньше")

print("Угадал!")