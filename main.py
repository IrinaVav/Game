field = [[' ', ' ', ' '] for i in range(3)]


def greet():
    print('Добро пожаловать в игру!')
    print('Для того чтобы сделать ход введите две координаты.')


def playing_field():
    print(f'   0   1   2')
    print(f'  ---', '---', '---')
    for i in range(3):
        print(f'{i}| {field[i][0]} | {field[i][1]} | {field[i][2]} |')
        print(f'  ---', '---', '---')


def ask():
    while True:
        coordinates = input('Введите координаты через пробел: ').split()

        if len(coordinates) != 2:
            print('Введите две координаты.')
            continue

        x, y = coordinates
        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Введены неверные координаты! Повторите ввод.')
            continue
        if field[x][y] != ' ':
            print('Клетка занята! Повторите ввод.')
            continue

        return x, y


def win():
    win_combination = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
                       ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                       ((1, 0), (1, 1), (2, 1)), ((2, 0), (2, 1), (2, 2)),
                       ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]

    for winner in win_combination:
        combination = []
        for a in winner:
            combination.append(field[a[0]][a[1]])
        if combination == ['X', 'X', 'X']:
            print('Выиграл Крестик!')
            return True
        if combination == ['O', 'O', 'O']:
            print('Выиграл Нолик!')
            return True
    return False


greet()

move = 0

while True:
    move += 1
    playing_field()

    if move % 2 == 1:
        print('Ходит Крестик.')
    else:
        print('Ходит Нолик.')

    x, y = ask()

    if move % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'

    if win():
        break

    if move == 9:
        print('Ничья')
        break
