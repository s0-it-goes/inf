email    :str = input('Email: ')
password :str = input('Password: ')

emailReport = ""

if email.count('@') != 1:
    emailReport += "x @ встречается больше одного раза, либо отсутствует\n"

if email.rfind('@') > email.rfind('.'):
    emailReport += "x не содержит . после @\n"

if (email.find('@') == 0 or email.find('@') == len(email) - 1) or (email.find('.') == 0 or email.find('.') == len(email) - 1):
    emailReport += "x email начинается или заканчиваетя на . или @\n"

if len(email) > 30 or len(email) < 6:
    emailReport += "x Длина email некорректна\n"

if emailReport:
    print("Email: " + email + " -> \n" + emailReport)
else:
    print("Email: " + email + " -> OK!")

passwordReport = ""

if len(password) < 8:
    passwordReport += "x слишком короткий\n"

if not('1' in password or '2' in password or '3' in password or '4' in password or '5' in password or '6' in password \
       or '7' in password or '8' in password or '9' in password or '0' in password):
    passwordReport += "x нет цифры\n"

if not('A' in password or 'B' in password or 'C' in password or 'D' in password or 'E' in password or 'F' in password or 'G' in password \
       or 'H' in password or 'I' in password or 'J' in password or 'K' in password or 'L' in password or 'M' in password or 'N' in password \
        or 'O' in password or 'P' in password or 'Q' in password or 'R' in password or 'S' in password or 'T' in password or 'U' in password \
            or 'V' in password or 'W' in password or 'X' in password or 'Y' in password or 'Z' in password):
    passwordReport += "x нет заглавной буквы\n"

if not('a' in password or 'b' in password or 'c' in password or 'd' in password or 'e' in password or 'f' in password or 'g' in password \
       or 'h' in password or 'i' in password or 'j' in password or 'k' in password or 'l' in password or 'm' in password or 'n' in password \
        or 'o' in password or 'p' in password or 'q' in password or 'r' in password or 's' in password or 't' in password or 'u' in password \
            or 'v' in password or 'w' in password or 'x' in password or 'y' in password or 'z' in password):
    passwordReport += "x нет строчной буквы\n"

if not('!' in password or '@' in password or '#' in password or '$' in password or '%' in password or '^' in password \
       or '&' in password or '*' in password):
    passwordReport += "x нет спецсимвола\n"

if passwordReport:
    print("Password: " + password + " -> \n" + passwordReport)
else:
    print("password: " + password + " -> OK!")