a :bool = bool(int(input()))
b :bool = bool(int(input()))
c :bool = bool(int(input()))
d :bool = bool(int(input()))

isLocked :bool = False

if a == 1 and d == 1:
    isLocked = True
elif (a and (not b)) or (c and d):
    isLocked = False

print("CLOSED" if isLocked else "OPEN")