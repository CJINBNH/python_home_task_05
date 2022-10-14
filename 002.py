# Задача №2 Создайте программу для игры в ""Крестики-нолики"".
import random
def check_x(pole):
    if pole[0][0] == 'x' and pole[1][1] == 'x' and pole[2][2] == 'x':
        print('Вы выиграли')
        return True
    elif pole[2][0] == 'x' and pole[1][1] == 'x' and pole[0][2] == 'x':
        print('Вы выиграли')
        return True
    elif pole[0][0] == 'x' and pole[1][0] == 'x' and pole[2][0] == 'x':
        print('Вы выиграли')
        return True
    elif pole[0][0] == 'x' and pole[0][1] == 'x' and pole[0][2] == 'x':
        print('Вы выиграли')
        return True
    elif pole[0][1] == 'x' and pole[1][1] == 'x' and pole[2][1] == 'x':
        print('Вы выиграли')
        return True
    elif pole[1][0] == 'x' and pole[1][1] == 'x' and pole[1][2] == 'x':
        print('Вы выиграли')
        return True
    elif pole[0][2] == 'x' and pole[1][2] == 'x' and pole[2][2] == 'x':
        print('Вы выиграли')
        return True
    elif pole[2][0] == 'x' and pole[2][1] == 'x' and pole[2][2] == 'x':
        print('Вы выиграли')
        return True
    else:
        return False
def check_o(pole):
    if pole[0][0] == 'o' and pole[1][1] == 'o' and pole[2][2] == 'o':
        print('Компьютер победил')
        return True
    elif pole[2][0] == 'o' and pole[1][1] == 'o' and pole[0][2] == 'o':
        print('Компьютер победил')
        return True
    elif pole[0][0] == 'o' and pole[1][0] == 'o' and pole[2][0] == 'o':
        print('Компьютер победил')
        return True
    elif pole[0][0] == 'o' and pole[0][1] == 'o' and pole[0][2] == 'o':
        print('Компьютер победил')
        return True
    elif pole[0][1] == 'o' and pole[1][1] == 'o' and pole[2][1] == 'o':
        print('Компьютер победил')
        return True
    elif pole[1][0] == 'o' and pole[1][1] == 'o' and pole[1][2] == 'o':
        print('Компьютер победил')
        return True
    elif pole[0][2] == 'o' and pole[1][2] == 'o' and pole[2][2] == 'o':
        print('Компьютер победил')
        return True
    elif pole[2][0] == 'o' and pole[2][1] == 'o' and pole[2][2] == 'o':
        print('Компьютер победил')
        return True
    else:
        return False
pole = [["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]]
for i in pole:
    print(i)
def convert_for_x(a):
    global pole
    if a == 1 and pole[0][0] == '_':
        pole[0][0] = 'x'
        for i in pole:
            print(i)
            print('Ход компьютера')
    elif a == 2 and pole[0][1] == '_':
        pole[0][1] = 'x'
        for i in pole:
            print(i)
            print('Ход компьютера')
    elif a == 3 and pole[0][2] == '_':
        pole[0][2] = 'x'
        for i in pole:
            print(i)
            print('Ход компьютера')
    elif a == 4 and pole[1][0] == '_':
        pole[1][0] = 'x'
        for i in pole:
            print(i)
            print('Ход компьютера')
    elif a == 5 and pole[1][1] == '_':
        pole[1][1] = 'x'
        for i in pole:
            print(i)
            print('Ход компьютера')
    elif a == 6 and pole[1][2] == '_':
        pole[1][2] = 'x'
        for i in pole:
            print(i)
            print('Ход компьютера')
    elif a == 7 and pole[2][0] == '_':
        pole[2][0] = 'x'
        for i in pole:
            print(i)
            print('Ход компьютера')
    elif a == 8 and pole[2][1] == '_':
        pole[2][1] = 'x'
        for i in pole:
            print(i)
            print('Ход компьютера')
    elif a == 9 and pole[2][2] == '_':
        pole[2][2] = 'x'
        for i in pole:
            print(i)
            print('Ход компьютера')
    else:
        print('Укажите значение от 1 до 9 для свободной клетки')
        convert_for_x(int(input()))

while not check_x(pole) and not check_o(pole):
    a = int(input())
    convert_for_x(a)
    while True:
        c, d = random.randint(0, 2), random.randint(0, 2)
        if pole[c][d] == '_':
            break
    pole[c][d] = 'o'
    for i in pole:
        print(i)