
x :int = int(input())

if x > 230 or x < 0:
    print("Ввод выходит за диапазон значений 0 -- 230")
    x = int(input)

heights :list = [x]

print("Рост каждого человека в строю, для выхода введите 0")

usr_input = 1;

while usr_input:
    usr_input = int(input())
    heights.append(usr_input)

heights.pop() #удаляю последний элемент, т.к. он равен 0

heights.sort(reverse=True)

pos = 0

if x in heights:
    for i in range(len(heights)):
        if x == heights[i]:
            pos = i
else:
    print("pos:", heights.index(x) + 1)

print("pos: ", pos + 1)