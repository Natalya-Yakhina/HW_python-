# 5. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


spisok = [2, 3, 4, 5, 6]
# spisok = [2, 3, 5, 6]


def pairs_num(spisok):
    count = (len(spisok) + 1) // 2
    result = []
    for i in range(count):
        result.append(spisok[i] * spisok[-(i + 1)])
    return result

result = pairs_num(spisok)
print(spisok, '=>', result)