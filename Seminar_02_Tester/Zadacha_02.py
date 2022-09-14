# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input("Введите число N = "))
# result = 1
# result_list = []
# for i in range(1, N + 1): # range - возвращает объект, который производит последовательность целых чисел от начала до остановки пошагово.
#     result *= i
#     result_list.append(result) # append - добавляет объект в конец списка
# print(result_list)

number = input('Введите число: ')
sum = 0
for i in number:
    if i.isdigit():
        sum += int(i)
print(int(sum))