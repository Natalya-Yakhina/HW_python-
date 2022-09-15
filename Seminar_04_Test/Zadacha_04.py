# 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = [random.randint(1, 100) for i in range(random.randint(2, 10))]
print('Натуральная степень: n =', len(k)-1)

m = ''
for i in range(0, len(k)):
    m = m + str(k[i])
    if i < len(k) - 1:
        m = m + 'x'
    if i < len(k) - 2:
        m = m + '^' + str(len(k) - i - 1)
    if i < len(k) - 1:
        m = m + '+'
m = m + ' = 0'
print(m)