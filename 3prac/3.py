str = input("Введите строку: ")
print("Символов в строке: ", len(str))
print("Байтов в UTF-8: ", len(str.encode("UTF-8")))
print("Байтов в CP1251: ", len(str.encode("CP1251")))