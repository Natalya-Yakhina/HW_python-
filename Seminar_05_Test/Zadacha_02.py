# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

# from curses.ascii import isdigit
import random

print('Условия игры: ')
print('На столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет.')
print('Выигрывает и забирает все конфеты тот, кто заберет ПОСЛЕДНЮЮ конфету!')
print()

player1 = input('Игрок-1, введите имя:\n')
player2 = input('Игрок-2, введите имя: \n')
players = [player1, player2]

total_candy = 2021
take_max = 28

right_of_way = random.randint(0,5) # число для права хода
# проверка на ввод числа при жеребьевке
while True:
    conceived = input('Введите "0" если считаете что число четное, "1" - если нечетное: ') # предположение игрока
    if conceived.isdigit(): # возвращает True, если все символы являются цифрами, иначе False.
        conceived = int(conceived)
        break
    else:
        print('Ошибка ввода! Введите еще раз!')

print('Было загаданно число: ', right_of_way)






# print('Мы загадали число от 1 до 10. Ваша задача - угадать четное это число или нет.')
# print('Право первого хода предоставляется игроку отгадавшему число')
# candies = 2021
# take_max = 28
# whos_turn = randint(1,10)
# while True:
#     guess = input('Введите 0, если считаете, что число четное, 1 - число нечетное: ')
#     if guess.isdigit():
#         guess = int(guess)
#         break
#     else:
#         print('Некорректный ввод. Повторите')

# print('Было загадано число', whos_turn)
# if guess == 0 and whos_turn%2==0:
#     print('Вы угадали. Право первого хода за вами')
# elif guess ==1 and whos_turn%2!=0:
#     print('Вы угадали. Право первого хода за вами')
# else:
#     print('Первый ход делает ваш оппонент')  

# players = []
# print('Введите имена игроков.')
# players.append(input('Игрок 1: '))
# players.append(input('Игрок 2: '))
# player = 0  

# while candies > 0:
#     print(f'{players[player]}, cколько конфет вы бы хотели взять? ')
#     take = int(input())

#     if 0 < take <= take_max and take<=candies:
#         if player == 0: player = 1
#         elif player == 1: player = 0
#         candies -= int(take)
#         print(f'Осталось {candies} конфет')
#     else: print('Вы ввели неверное число!')

# if candies == 0:
#     if player == 1:
#         print(f'Ура! {players[0]}, вы выиграли!')
#     elif player == 0:
#         print(f'Поздравляем, {players[1]},  вы выиграли!')



# ==============================================================

# import random

# greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
#     'Основные правила игры: '
#     'Нам будет дано некоторое количество конфет, '
#     'за один ход мы можем взять не более определённого количества, '
#     'о котором мы с вами договоримся.'
#     'Итак, начнём!')
            

# messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
#             'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


# def play_game(n, m, players, messages):
#     count = 0
#     if n%10 == 1 and 9 > n > 10: letter = 'а'
#     elif 1 < n%10 < 5 and 9 > n > 10: letter = 'ы'
#     else: letter = ''
#     while n > 0:
#         print(f'{players[count%2]}, {random.choice(messages)}')
#         move = int(input())
#         if move > n or move > m:
#             print(f'Это слишком много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
#             attempt = 3
#             while attempt > 0:
#                 if n >= move <= m:
#                     break
#                 print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
#                 move = int(input())
#                 attempt -=1
#             else: 
#                 return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
#         n = n - move
#         if n > 0: print(f'Осталось {n} конфет{letter}')
#         else: print('Все конфеты разобраны.')
#         count +=1
#     return players[not count%2]

# print(greeting)

# player1 = input('Давайте познакомися. Первый игрок, как к Вам можно обращаться?\n')
# player2 = input('Второй игрок, и Вы представьтесь, пожалуйста\n')
# players = [player1, player2]

# n = int(input('Сколько конфет будем разыгрывать?\n '))
# m = int(input('Сколько максимально будем брать конфет за один ход?\n '))

# winer = play_game(n, m, players, messages)
# if not winer:
#     print('У нас нет победителя.')
# else: print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')