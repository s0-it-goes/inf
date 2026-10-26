grades :list = [" 5 ", "неявка", "4", " хор ", "", "100", "2", "два"]
i :int = 0
while(i < len(grades)):
    match grades[i].strip():
        case 'отл' | '5':
            grades[i] = 5
        case 'хор' | '4':
            grades[i] = 4
        case 'уд' | '3':
            grades[i] = 3
        case 'неуд' | '2':
            grades[i] = 2
        case _:
            grades.pop(i)
            i -= 1
    i += 1

print(grades)