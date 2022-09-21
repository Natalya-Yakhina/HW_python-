# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


# ======================================  игра с жеребъевкой =======================================================
print("*" * 15, " ИГРА КОНФЕТЫ ", "*" * 15)
import random

print()
print( 'Условия игры: \n'
        'На столе лежит 2021 конфета. \n' 
        'За один ход можно забрать не более чем 28 конфет. \n'
        'Выигрывает и забирает все конфеты тот, кто заберет ПОСЛЕДНЮЮ конфету!\n')

total_candy = 2021 # всего конфет
take_max = 2020 # максимальное число конфет за один ход

# ===== жеребьевка на право хода =====
print('Начнем жеребьёвку: \n')
lottery = random.randint(0,5) 

while True: # проверка на ввод числа при жеребьевке
    conceived = input('Введите "0" если считаете что число четное, "1" - если нечетное: ') # предположение игрока
    if conceived.isdigit(): # возвращает True, если все символы являются цифрами, иначе False.
        conceived = int(conceived)
        break
    else:
        print('Ошибка ввода! Введите еще раз!')

print('Было загаданно число: ', lottery)

if conceived == 0 and lottery % 2 == 0: # если загаданное число четное и выпало четное
    print('Вы угадали! Вы ходите первым :)')
elif conceived == 1 and lottery % 2 != 0: #  загаданное число нечетное и выпало нечетное
    print('Вы угадали! Вы ходите первым :)')
else:
    print('Вы ошиблись! Ход соперника :(')

# ======== ввод игроков ==========
players = [] # список игроков
print('Введите имена игроков:')
players.append(input('Игрок-1, введите имя: \n')) 
players.append(input('Игрок-2, введите имя: \n')) 
player = 0

while total_candy > 0: # если количество конфет больше нуля
    print(f'{players[player]} Сколько конфет хотите взять?') # Чтобы выводил имя игрока
    take = int(input())

    if 0 < take <= take_max: # взяли больше 0 но меньше мах
        if player == 0: player = 1 # переход хода 
        elif player == 1: player = 0
        total_candy -= int(take)
        print(f'Остаток конфет: {total_candy}')
    else:
        print("Ошибка! Столько конфет взять нельзя!")
        
if total_candy == 0: # если конфеты закончились
    if player == 1:
        print(f'Ура! {players[0]}, вы выиграли! Все конфеты Ваши!')
    # else:
    #     print(f'{players[0]} вы проиграли')
    elif player == 0:
        print(f'Поздравляем, {players[1]},  вы выиграли! Все конфеты Ваши!')


 # ======================================  игра с ботом =======================================================

# print("*" * 15, " ИГРА КОНФЕТЫ С БОТОМ ", "*" * 15)

# from random import randint, choice, random

# print()
# print('Условия игры: \n'
#         'На столе лежит 2021 конфета. \n' 
#         'За один ход можно забрать не более чем 28 конфет. \n'
#         'Выигрывает и забирает все конфеты тот, кто заберет ПОСЛЕДНЮЮ конфету!\n')

# messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', # сообщения игры в виде списка
#             'сколько конфет возьмёте?', 'берите конфеты, не стесняйтесь', 'Ваш ход', 'сколько вам еще конфет?']

# # # ======== функция ввода игроков ==========

# def players():
#     player1 = input('Игрок-1, введите имя: \n')
#     player2 = 'БОТ'
#     print(f'Игрок-2, {player2}')
#     return [player1, player2]

# # # ======== функция правил игры ==========

# def rules_of_the_game(players):

#     total_candy = 2021 # всего конфет
#     take_max = 28 # максимальное число конфет за один ход
#     first = int(input(f'{players[0]}, чтобы ходить первым нажми - 1, если нет - любую клавишу\n')) # выбор позиции хода
#     if first != 1:
#         first = 0
#     return [total_candy, take_max, int(first)]

# # # ======== функция игра ==========

# def play_game(rules, players, messages):
#     count = rules[2]
#     if rules[0] % 10 == 1 and 9 > rules[0] > 10:
#         letter = 'а'
#     elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
#         letter = 'ы'
#     else:
#         letter = ''
#     while rules[0] > 0:
#         if not count % 2:
#             move = randint(1, rules[1])
#             print(f'БОТ забирает: {move}')
#         else:
#             print(f'{players[0]}, {choice(messages)}') # choice - выбрает случайный элемент из последовательности (сообщения)
#             move = int(input()) # шаг игры
            
#             if move > rules[0] or move > rules[1]: # если количество взятых конфет больше заданного
#                 print(f'ОШИБКА! Можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}\n')
#                 attempt = 3 # количество попыток ввода
#                 while attempt > 0:
#                     if rules[0] >= move <= rules[1]:
#                         break
#                     print(f'Попробуйте ещё раз, у Вас осталось {attempt} попытки')
#                     move = int(input())
#                     attempt -= 1
#                 else:
#                     return print(f'Game over!') # закончились попытки - конец игры 
#         rules[0] -= - move
#         if rules[0] > 0:
#             print(f'Осталось {rules[0]} конфет{letter}')
#             print()
#         else:
#             print('Все конфеты разобраны!')
#         count += 1
#     return players[count % 2]

# players = players()
# rules = rules_of_the_game(players)

# winner = play_game(rules, players, messages)

# if not winner:
#     print('Победителя нет!') # если закончились попытки
# else:
#     print(
#         f'Поздравляю! Победил {winner}! Ему достаются все конфеты!')