def func(x:int):
    return x**2 / 10 + 1

N :int = int(input())

[a, b] = [-2, 5]

h :int = (b - a) / N
sum :float = 0
x = a + h

for i in range(1, N):
   sum += func(x)
   x += h 

sum *= h

sum += (h/2)*(func(a) + func(b))

print(sum)