s   :str = input()
a   :str = ''

for i in s:
    a += i if i.isalpha() else ''

print(a)