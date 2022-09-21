# 5. Создать программу, считывающую два полинома из двух файлов и записывающая в третий файл их сумму.


def sumPoly (polinomial1, polinomial2):
    for i in range(len(polinomial1)):
        for j in polinomial2:
            if polinomial1[i][1] == j[1]:
                polinomial1[i] = ((polinomial1[i][0] + j[0], polinomial1[i][1]))
                polinomial2.remove(j)
    sum = polinomial1 + polinomial2
    for i in sum:
        if i[0] == 0:
            sum.remove(i)
    sum = sorted(sum, key=lambda num: num[1])
    sum.reverse()
    return sum
    
with open("pol1.txt", "r") as f:
    П1 = []
    i = 0
    for line in f:
        lines = line.split(' ')
        lst = []
        for ln in lines:
            ln = ln.rstrip()
            if ln != '':
                num = int(ln)
                lst = lst + [num]
        П1 = П1 + [lst]
print("П1 = ", П1)

with open("pol2.txt", "r") as f2:
    П2 = []
    i = 0
    for line in f2:
        lines = line.split(' ')
        lst = []
        for ln in lines:
            ln = ln.rstrip()
            if ln != '':
                num = int(ln)
                lst = lst + [num]
        П2 = П2 + [lst]
print("П2 = ", П2)

res = open('sumPoly.txt', 'w')

result = sumPoly(П1, П2)

print(f'Сумма в виде списка кортежей: {result}')
res.write(str(result))

f.close()
f2.close()
res.close()