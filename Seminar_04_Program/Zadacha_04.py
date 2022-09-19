# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция. 
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. 
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


language = input('Выберите язык - aнгл = e, рус = r : ')
chif = input('Выберите шифрование: шифрование - ch, дешифрование - def: ')
n = int(input('Введите ключ шифрования: ')) # в данном условии = 1
f = input('Введите фразу: ')

def chru(chifr, n, l, fraza):
    if l == 'r':
        moch = 32 # размер русского алфавита
    if l == 'e':
        moch = 26 # размер английского алфавита
    if chifr== 'def':
        n = -n
    for i in range(len(fraza)):
        if fraza[i].isalpha():
            if fraza[i] == fraza[i].upper(): # upper - dозвращает копию исходной строки с символами приведёнными к верхнему регистру
                for j in range (moch):
                    if moch == 32:
                        if fraza[i] == rus_upper_alphabet[j]:
                            print(rus_upper_alphabet[(j + n) % moch], end = '')
                            break
                    if moch == 26:
                        if fraza[i] == eng_upper_alphabet[j]:
                            print(eng_upper_alphabet[(j + n) % moch], end = '')
                            break
            elif fraza[i] == fraza[i].lower(): # lower - преобразует все символы верхнего регистра в строке в символы нижнего регистра и возвращает их
                for j in range (moch):
                    if moch == 32:
                        if fraza[i] == rus_lower_alphabet[j]:
                           print(rus_lower_alphabet[(j + n) % moch], end='')
                           break
                    if moch == 26:
                        if fraza[i] == eng_lower_alphabet[j]:
                           print(eng_lower_alphabet[(j + n) % moch], end = '')
                           break
        else:
            print(fraza[i], end='')

chru(chif, n, language, f)



#=======================================================================================
# alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# sdvig = 1
# message = input("Сообщение для ДЕшифровки: ").upper()
# itog = ''
# languageg = input('Выберите язык RU/EU: ')
# if languageg == 'RU':
#     for i in message:
#         mesto = alfavit_RU.find(i)
#         new_mesto = mesto + sdvig
#         if i in alfavit_RU:
#             itog += alfavit_RU[new_mesto]
#         else:
#             itog += i
# else:
#     for i in message:
#         mesto = alfavit_EU.find(i)
#         new_mesto = mesto + sdvig
#         if i in alfavit_EU:
#             itog += alfavit_EU[new_mesto]
#         else:
#             itog += i
# print (itog)
#=======================================================================================