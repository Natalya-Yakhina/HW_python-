# 5. Реализуйте алгоритм перемешивания списка.

import random

n = int(input("Введите размер списка: "))
a = []
for i in range(n):
    newElem = random.randint(0, n) # randint - Возвращает случайное целое число в диапазоне [a, b], включая обе конечные точки.
    a.append(newElem)
print(f"Cписок: {a}")
random.shuffle(a) # shuffle - перемешивает список
print(f"Перемешанный список: {a}")


# import random # генерация случайных чисел
# list = [1, 2, 3, 4, 5]
# result = random.sample(list, len(list)) # sample - возвращает новый список, содержащий элементы из совокупности, оставляя исходную совокупность без изменений. 
# print ("\n", str(list), "-->", str(result))
