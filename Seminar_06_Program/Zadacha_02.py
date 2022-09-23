# 2- Найти сумму чисел списка стоящих на нечетной позиции

from unittest import result

spisok = [2, 3, 5, 9, 3]

# result = list(filter(lambda x: x % 2, spisok)) # нечетные элементы

num_poz = [i for i in range(1, len(spisok)) if not i % 2 == 0] # нечетные значения из списка
num_poz = [v for k,v in enumerate(spisok) if not k % 2 == 0] # четные значения ключей из массива
# lst = list(enumerate(spisok)) # чтобы понимать как это работает [(0, 2), (1, 3), (2, 5), (3, 9), (4, 3)]
print('\n', spisok, '-> на нечётных позициях элементы ', num_poz, ', сумма которых =', sum(num_poz))