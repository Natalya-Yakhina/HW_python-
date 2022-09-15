# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

n = int(input('Задайте натуральное число: '))

def Factorization(n): # функция факторизации перебором делителей
    divisor = [] # список делителей
    d = 2 # делитель
    while d * d <= n:
        if n % d == 0:
            divisor.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        divisor.append(n)
        return divisor

print(f'Простые множители числа {n} -> {Factorization(n)}')