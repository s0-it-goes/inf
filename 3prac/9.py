s = input()

if (len(s) == 6 and s[:3].isalpha and s[3:6].isdigit()):
    print("Old format")
elif (len(s) == 7 and s[:4].isdigit and s[4:7].isalpha()):
    print("New format")
else:
    print("Wrong input")