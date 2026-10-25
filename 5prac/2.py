N :int = int(input())
a :str = ""

if(N <= 0):
    print("Wrong input")
else:
    for i in range(0, N):
        a += (N - 1 - i) * ' '
        a += (i * 2 + 1) * '#'

        print(a)
        a = ""

    print((N - 1) * ' ' + '#')
