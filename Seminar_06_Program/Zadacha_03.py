# 3 - Найти расстояние между двумя точками пространства(числа вводятся через пробел)

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt

xA,yA = map(int,(input("Введите координаты X и Y точки A через пробел: ").split()))
xB,yB = map(int,(input("Введите координаты X и Y точки В через пробел: ").split()))

AB = round(sqrt((xA - xB)**2 + (yA - yB)**2), 2)
print('Расстояние между двумя точками А и В =', round(AB -0.005, 2))