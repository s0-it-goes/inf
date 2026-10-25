line1 :str = input()
line2 :str = input()
line3 :str = input()

def isHaiku(line :str, syllable :int):
    cnt     :int = 0
    vowels  :str = 'аеёиоуыэюя'

    for s in line:
        if s.lower() in vowels:
            cnt += 1
    
    if cnt == syllable:
        return True

    return False

if isHaiku(line1, 5) and isHaiku(line2, 7) and isHaiku(line3, 5):
    print("Хайку!")
elif len(line1) == 0 or len(line2) == 0 or len(line3) == 0:
    print("Не хайку. Должно быть 3 строки")
else:
    print("Не хайку")