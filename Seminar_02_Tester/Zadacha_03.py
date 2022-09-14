# 3. Задайте список из n чисел последовательности 
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input("Введите размер списка: n = "))
# sumElem = 0
# a = []

# for i in range(n):
#     new_elem = (1+1/(i+1)**(i+1))
#     a.append(new_elem)
# print(f"Список: {a}")

# sumElem = sum(a)
# print(f"Сумма чисел списка = {sumElem}")

n = int(input('Введите число: '))
lst = [round((1 + 1 / i) ** i, 5) for i in range(1, n + 1)] # сразу добавляем список
print(f'Список: {lst}')
print(f'Сумма чисел списка: {round(sum(lst), 5)}')