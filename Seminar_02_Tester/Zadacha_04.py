# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
n = int(input('Введите число N - '))
numbers = []
for i in range(n):
    numbers.append(randint(-n, n+1))
print(numbers)

f = open('file.txt', 'w')
while True:
    s = input('Укажите позицию для вычисления - ')
    if s == "":
        break
f.write(s+"\n")
f.close()

result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
result *= numbers[int(line)]
f.close()
print(result)