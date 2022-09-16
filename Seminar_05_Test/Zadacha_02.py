# # Создайте программу для игры с конфетами человек против человека.
# from random import randint

# print('Условия игры: ')
# print('На столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет.')
# print('Выигрывает тот, кто заберет ПОСЛЕДНЮЮ конфету. Он же забирает и все конфеты противника')
# print()
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