def palindrome(str):
    str = (str.strip()).lower()
    print(str)

    if str == str[::-1]:
        return True
    
    return False

def countVowel(str):
    cnt = 0
    for i in str:
        cnt += 1 if i in 'aeiou' else 0

    return cnt

def isEmail(str):
    cnt = 0
    for i in str:
        if i == '@':
            cnt = 1
        if cnt == 1 and i == '.':
            return True

    return False

def cutDomain(str):
    i = str.find('@')
    if str.find('@') != -1:
        return str[i+1:]
    
    return False

message :str = input()

print("Меню действий: \n1.Проверка на палиндром\n2.Подсчёт гласных\n3.Проверка только цифры\n4.Проверка только буквы\n" \
    "5.Переворот строки\n6.Верхний регистр\n7.Нижний регистр\n8.Замена пробелов на _\n9.Проверка на email\n10.Извлечение домена\n" \
    "11.Выход")

choice :int = 0

while(choice != 11):
    choice = int(input())
    
    match (choice):
        case 1:
            print("Сообщение является палиндромом!" if palindrome(message) else "Сообщение не является палиндромом")
        case 2:
            print("Количество гласных: " + str(countVowel(message)))
        case 3:
            print("В сообщении только цифры" if message.isdigit() else "В сообщении не только цифры")
        case 4:
            print("В сообщении только буквы" if message.isalpha() else "В сообщении не только буквы")
        case 5:
            print("Перевёрнутое сообщение: " + message[::-1])
        case 6:
            print("Сообщение в верхнем регистре: " + message.upper())
        case 7:
            print("Сообщение в нижнем регистре: " + message.lower())
        case 8:
            print("Замена пробелов в сообщении на _: " + message.replace(' ', '_'))
        case 9:
            print("Сообщение является email'ом" if isEmail(message) else "Сообщение не является email'ом")
        case 10:
            print("Домен: " + cutDomain(message) if cutDomain(message) else "Не является доменом")
        case 11:
            print("Выход из программы...")
        case _:
            print("Некорректный ввод")