letter1 :str = input()
num1    :int = int(input())
letter2 :str = input()
num2    :int = int(input())

chess = 'ABCDEFGH'

if  (letter1.upper() in chess) and\
(letter2.upper() in chess) and (num1 > 0 and num1 < 9) and\
(num2 > 0 and num2 < 9):
    pos1 = chess.find(letter1.upper()) + 1
    pos2 = chess.find(letter2.upper()) + 1

    if abs(num1 - num2) == abs(pos1-pos2):
        print("YES")
    else:
        print("NO")
        
else:
    print("WRONG INPUT")