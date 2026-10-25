s :str = input()

def decoder(code):
    if code[-1] != '#':
        return False

    code = code[0:-1]
    return code[0::2] + code[1::2][::-1]

print(decoder(s))