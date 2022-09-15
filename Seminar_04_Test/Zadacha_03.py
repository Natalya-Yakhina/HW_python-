# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


# =============== 1 способ =======================================================
# list1 = [1, 2, 3, 5, 1, 5, 3, 10, 15, 42]
# listNew = list(set(list1))# Создает неупорядоченную коллекцию уникальных элементов

# print(listNew)
# ================================================================================

# list = [1, 2, 3, 5, 1, 5, 3, 10, 15, 42]

# def sort_list(arg_list):
#     result = []
#     while arg_list:
#         temp = arg_list.pop(0)
#         if temp in arg_list:
#             while temp in arg_list:
#                 arg_list.remove(temp)
#         else:
#             result.append(temp)
#     return result

# new_list_input = sort_list(list)
# print(f"Список неповторяющихся элементов: {new_list_input}")



# import random
# n = int(input('Введите размерность исходной последовательности: '))

# def list_compl(n):
#     worc_list = []
#     for i in range(n):
#         worc_list.append(random.randint(1, 9))
#     return worc_list
# first_list = list_compl(n)
# print(first_list)

# second_list = set(first_list)
# print(second_list)


numbers_list = [1, 2, 3, 5, 1, 5, 3, 10]
unique_numbers_list = set(numbers_list)

print(f'Уникальные элементы в списке {numbers_list} - {unique_numbers_list}')