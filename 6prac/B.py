
sells = [1, 5, 2, 4, 3]

for i in range(1, len(sells)):
    if(sells[i] > sells[i-1]):
        print(sells[i], end=" ")

print()