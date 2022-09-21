# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход
# определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
# сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

import random

total_candys = 2021

def lottery():
    return random.randint(0, 100)

player1 = lottery()
player2 = lottery()

print(f'Выпал жребий {player1} Игроку 1!')
print(f'Выпал жребий {player2} Игроку 2!', '\n')


def loser():
    return random.randint(1, 28)

def winner(candys):
    if candys % 29 == 0:
        return candys % 29 + 28
    else:
        return candys % 29


if player1 > player2:
    print('Игрок 1 ходит первым!', '\n')
    player1 = winner(total_candys)
    total_candys = total_candys - player1
    print(f'Игрок 1 взял {player1} конфет! Осталось {total_candys} конфет! Ход Игрока 2!')
    while total_candys > 29:
        player2 = loser()
        total_candys = total_candys - player2
        print(f'Игрок 2 взял {player2} конфет! Осталось {total_candys} конфет! Ход Игрока 1!')
        player1 = winner(total_candys)
        total_candys = total_candys - player1
        print(f'Игрок 1 взял {player1} конфет! Осталось {total_candys} конфет! Ход Игрока 2!')
    player2 = loser()
    total_candys = total_candys - player2
    print(f'Игрок 2 взял {player2} конфет! Осталось {total_candys} конфет! Ход Игрока 1!')
    player1 = total_candys
    total_candys = total_candys - player1
    print(f'Игрок 1 взял {player1} конфет! Осталось {total_candys} конфет!', '\n')
    print('Игрок 2 проиграл!')

else:
    print('Игрок 2 ходит первым!', '\n')
    player2 = loser()
    total_candys = total_candys - player2
    print(f'Игрок 2 взял {player2} конфет! Осталось {total_candys} конфет! Ход Игрока 1!')
    while total_candys > 29:
        player1 = winner(total_candys)
        total_candys = total_candys - player1
        print(f'Игрок 1 взял {player1} конфет! Осталось {total_candys} конфет! Ход Игрока 2!')
        player2 = loser()
        total_candys = total_candys - player2
        print(f'Игрок 2 взял {player2} конфет! Осталось {total_candys} конфет! Ход Игрока 1!')
    player1 = total_candys
    total_candys = total_candys - player1
    print(f'Игрок 1 взял {player1} конфет! Осталось {total_candys} конфет!', '\n')
    print('Игрок 2 проиграл!')

