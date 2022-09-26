# 6. Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.


# N = int(input("Введите число: "))
# print(f"Для N = {N} -> ", end = "")
# for i in range(0, N-1):
#     print((-3)**i, end= ", ")
# else:
#     print((-3)**(N-1))


N = int(input("Введите число: "))
print(list(map(lambda x: (-3)**x, range(N))))