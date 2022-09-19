# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'Напишите абв програбву программу удаляющуабв удаляющую из текста все слова словабв, содержащие абв'

def delete(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return ' '.join(text)

text = delete(text)
print(text)

# ===================================================================================
# newTxt = 'Напишите абв програбву программу удаляющуабв удаляющую из текста все слова словабв, содержащие абв'.split()
# my_str = 'абв'
# result = list(filter(lambda x: not my_str in x, newTxt))
# print(result)
# ===================================================================================
# with open("words.txt", "r") as fin:
#     for line in fin:
#         words = line.split()
#     for word in words:
#         if "абв" in word:
#             words.remove(word)
# sentence = " ".join(words)
# print(sentence)
