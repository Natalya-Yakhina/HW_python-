# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений 
# (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input("Введите число N = "))


def input_numbers(input_text): # функция проверки на ввод числа
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{input_text}"))
            is_OK = True
        except ValueError:
                print("Ошибка! Это не число!")
    return number

N = input_numbers("Введите число: ")
result = 1
result_list = []
for i in range(1, N + 1):
        result *= i
        result_list.append(result) # append - добавляет объект в конец списка
print(result_list)