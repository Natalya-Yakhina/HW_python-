# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)


from datetime import datetime
import time, math

def randome(min, max):
    d = max - min # берем промежуток, разницу между мин и макс
    ms = datetime.today().microsecond / (10 ** 6)
    print(f"{ms}")
    return min + math.ceil(d * ms) # math.ceil округление

print(randome(0,10))
