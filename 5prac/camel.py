s :str = input()

def camelToSnake(s :str):
    for i in s:
        if i.upper() == i:
            index = s.find(i)
            s = s[:index] + '_' + s[index].lower() + (s[index+1:])

    return s

print(camelToSnake(s))