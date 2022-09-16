# Напишите программу, удаляющую из текста все слова, содержащие "абв".


# text=list(map(str,input('Введите текст: ').split()))
# text=' '.join(text)
# print(text)

# def delete_words(text):
#     text = list(filter(lambda x: 'абв' not in x, text.split()))
#     return " ".join(text)


# text = delete_words(text)
# print(text)


# Напишите программу, удаляющую из текста все слова, содержащие "абв"

newTxt = 'забвение бывает временным когда абв это называется самозабвением'.split()
my_str = 'абв'
result = list(filter(lambda x: not my_str in x, newTxt))
print(result)