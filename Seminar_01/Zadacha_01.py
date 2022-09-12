# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


def input_numbers(input_text): # функция проверки на ввод числа
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{input_text}"))
            is_OK = True
        except ValueError:
                print("Ошибка! Это не число!")
    return number

num = input_numbers("Введите номер дня недели: ")

if (num < 1 or num > 7):
    print("Ошибка!")
elif (num >= 1 and num <= 5):
    print("Нет, это рабочий день")
else:
    print( "Да, это выходной день")