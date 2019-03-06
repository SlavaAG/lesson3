with open('referat.txt', 'r', encoding = 'utf-8') as text_file:
    text = text_file.read()
    print("Длина строки ", len(text))
    words = text.split()
    print("Количество слов ", len(words))
    print(text)
    

with open('referat2.txt', 'w', encoding = 'utf-8') as content:
    text = text.replace('.', '!')
    content.write(text)