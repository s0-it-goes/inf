card = input()

digits = [int(d) for d in card]

sum = 0;

for i in range(0, len(digits)):
    sum += int(digits[i]) if i % 2 == 1 else 0
    if i % 2 == 0:
        sum += int(digits[i]) * 2 if int(digits[i]) * 2 < 10 else (int(digits[i]) * 2) - 9

if sum % 10 == 0:
    print("Корректный номер")
else:
    print("Некорректный номер")