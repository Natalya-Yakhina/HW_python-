# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# попытка разобрать увиденное на семинаре(

# def SumPolinom(polynom1, polynom2):
#     for i in range(len(polynom1)):
#         for j in polynom2:
#             if polynom1[i][1] == [j][1]:
#                 polynom1[i] = ((polynom1[i][0] + polynom2[j][0], polynom1[i][1]))
#                 polynom2.remove(j)
#     sum = polynom1 + polynom2
#     for i in sum:
#         if i[0] == 0:
#             sum.remove(i)
#         sum = sorted(sum, key=lambda num: num[1]) # Вернуть новый список, содержащий все элементы из итерации в порядке возрастания.
#         sum.reverse()
#         return sum

# file1 = open('polynom1.txt', 'r')
# f1 = file1.readline()
# file2 = open('polynom2.txt', 'r')
# f2 = file2.readline()
# res = open('sumpolynom.txt', 'w')

# result = SumPolinom(f1, f2)
# print(f'Сумма многочленов: {result}')
# res.write(str(result))
# file1.close()
# file2.close()
# res.close()