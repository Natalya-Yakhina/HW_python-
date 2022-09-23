# 1. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.
# ['апап4', 'fdgg3', 'fgdf', '6', 'fg24'] - ищем 24 - найдено на 4 индексе

# Функция проверки ввода числа.

def CheckNum(type_date=int, massage="Input number: "):
    while True:
        try:
            num = type_date(input(massage))
            break
        except ValueError:
            print('It is not correct number. Try again.')
    return num

list_arr = ['апап4', 'fdgg3', 'fgdf', '6', 'fg24']
num = CheckNum()
# count = 0
for i in range(len(list_arr)):
    if str(num) in list_arr[i]:
        count = i
        break
try:
    print(count)
except:
    print("Такого числа нет.")