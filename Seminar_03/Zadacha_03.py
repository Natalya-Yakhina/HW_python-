# 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]

def dif_max_min (list):
    new_list = []
    for i in range(len(list)):
        if type(list[i]) is float:
            list[i] = round(float(list[i]) - int(list[i]), 3)
            new_list.append(list[i])

    new_list.sort()
    if len(new_list) == 0:
        return 0
    elif len(new_list) == 1:
        return new_list[0]
    else:
        result = new_list[-1] - new_list[0]
    return result

print(list, ' => ', dif_max_min(list))