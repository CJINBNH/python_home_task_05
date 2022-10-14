# Задача №1 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

import random
print('Не останься последним!')
sweets = 117
corch = random.randint(0, 1)
while sweets > 0:
    if corch == 1:
        yourMove = int(input('Сколько конфет возьмёте? - '))
        if 1 <= yourMove < 29 and sweets - yourMove >= 0:
            sweets -= yourMove
            print("осталось: ", sweets)
            corch = 0
        else:
            print('Взять можно только те конфеты что остались, но не более 28 шт')
            corch = 1
    else:
        if 114 < sweets <= 142:
            comp = 2
            sweets -= comp
            print('Компьютер берёт', comp)
            print('осталось', sweets)
            corch = 1
        elif 86 <= sweets <= 114:
            comp = sweets - 88
            if comp >= 1:
                sweets -= comp
                print('Компьютер берёт', comp)
                print('осталось', sweets)
                corch = 1
            else:
                comp += 1
                sweets -= comp
                print('Компьютер берёт', comp)
                print('осталось', sweets)
                corch = 1
        elif 59 <= sweets <= 86:
            comp = sweets - 59
            if comp >= 1:
                sweets -= comp
                print('Компьютер берёт', comp)
                print('осталось', sweets)
                corch = 1
            else:
                comp += 1
                sweets -= comp
                print('Компьютер берёт', comp)
                print('осталось', sweets)
                corch = 1
        elif 30 < sweets <= 58:
            comp = sweets - 30
            sweets -= comp
            print('Компьютер берёт', comp)
            print('осталось', sweets)
            corch = 1
        elif sweets == 30:
            comp = 1
            sweets -= comp
            print('Компьютер берёт', comp)
            print('осталось', sweets)
            corch = 1
        elif sweets <= 29:
            comp = sweets - 1
            if comp >= 1:
                sweets -= comp
                print('Компьютер берёт', comp)
                print('осталось', sweets)
                corch = 1
            else:
                comp += 1
                sweets -= comp
                print('Компьютер берёт', comp)
                print('осталось', sweets)
                corch = 1
if corch == 0:
    print('Проиграл игрок')
elif corch == 1:
    print('Бот проиграл')
