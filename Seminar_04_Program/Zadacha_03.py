# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».

# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

list_student = []
with open('student.txt', 'w', encoding='utf-8') as file_obg:
    for line in file_obg:
        if '5' in line:
            line = line.upper() # Возвращает копию строки, преобразованную в верхний регистр
        list_student.append(line.replace('\n', ''))
print(list_student)

with open('main.txt', 'w', encoding='utf-8') as file_obg:
    for line in list_student:
        file_obg.write(line + '\n')