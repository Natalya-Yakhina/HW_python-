# def choice():
#     print('\n ТЕЛЕФОННЫЙ СПРАВОЧНИК\n')
#     result = int(input('Выберете команду: \n\
#         1 - Ввести новый контакт\n\
#         2 - Поиск\n\
#         3 - Вывести полный список\n\
#         4 - Закончить работу\n\
#         Ваш выбор: '))
#     return result

def mod():
    print('\n ДОБРО ПОЖАЛОВАТЬ!\n')
    mod = int(input('Выберите режим: \n\
        1 - эспорт \n\
        2 - импорт '))
    return mod

def inpp():
    str_person = input('Введите данные для импорта: ')
    return str_person

def exp():
    second_name = input('Введите фамилию человека: ')
    return second_name