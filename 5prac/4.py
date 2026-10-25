text :str = input()
word :str = input()

tmp = ''

if(len(word) > len(text)):
    print(False)
else:
    for i in word:
        if i in text:
            text = text[text.find(i)+1:]
            tmp += i
            
    print(True if tmp == word else False)