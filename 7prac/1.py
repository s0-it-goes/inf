def func(x:int):
    return x**2 / 10 + 1

N :int = int(input())

[a, b] = [-2, 5]

h :int= (b - a) / N
sum :int = 0

for i in range(N):
   sum += func(a) * h
   a += h 

print(sum)