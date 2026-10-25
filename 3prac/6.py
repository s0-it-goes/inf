text = "Сообщение"
encoded_text = text.encode("UTF-8")
broken_text  = encoded_text.decode("CP1251")

print("Сломанный текст: ", broken_text)

def repairText(text):
    text = text.encode("CP1251")
    
    text = text.decode("UTF-8")
    return text

print(repairText(broken_text))