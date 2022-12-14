# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11


n = input("Введите число N = ")
sum = 0
for digit in n:
    if digit.isdigit(): # isdigit - возвращает True, если строка является строкой цифр
        sum += int(digit)
print(f"Сумма цифр введенного числа {n} = {sum}")


#  ====== только для натуральных чисел ==========
# n = float(input("Введите число N: "))
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     n = n // 10
# print (f"Сумма цифр введенного числа {n} = {sum}")