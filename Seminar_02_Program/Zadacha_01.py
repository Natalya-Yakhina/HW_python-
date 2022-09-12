# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными

# Пример:
# 67.82 -> 23
# 0.56 -> 11

n = input("Введите число N = ")
sum = 0
for digit in n:
    if digit.isdigit(): # isdigit - возвращает True, если строка является строкой цифр
        sum += int(digit)
print(f"Сумма цифр введенного числа {n} = {sum}")


# var = input("Введите число ")
# sum = 0
# var1 = None
# for i in var:
#     try:
#         var1 = int(i)
#     except:
#         continue
#     sum = sum + var1
# print("Sum=", sum)