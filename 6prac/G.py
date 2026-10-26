n :int = int(input())

arr = []

for i in range(n):
    arr.append(input())

print("Вывод:")
for i in range(n):
    word = arr[i]
    if len(word) > 10:
        arr[i] = word[0] + (str) (len(word) - 2) + word[-1]

    print(arr[i])