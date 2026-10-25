a = int(input())
b = int(input())
c = int(input())
d = int(input())

left = max(a, b)
right = min(c, d)

if left < right:
    print("Пересечение: ", left, right, "\nДлина: ", right - left, "\nПересечение имеет ненулевую длину")
elif left == right:
    print("Пересечение: точка")
else:
    print("Пересечние отсутствует")