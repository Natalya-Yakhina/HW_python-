# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

text = 'абвгдейка - это передача'

def delete(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return ' '.join(text)

text = delete(text)
print(text)
