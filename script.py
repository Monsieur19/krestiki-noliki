def input_coords():
    while True:
        coords = input('Введите координаты в формате: x y\n').split()

        x,y = coords
        x,y = int(x), int(y)

        return x,y

def step(x, y):
    global symb

    if field[x][y] == ' - ':
        field[x][y] = symb
    else:
        print('Поле уже занято')
        return

    print('   0  1  2')
    for i, row in enumerate(field):
        print(i, ''.join(row))

    if symb == ' x ':
        symb = ' o '
    else:
        symb = ' x '

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for i in win_cord:
        check_coords = []
        for j in i:
            check_coords.append(field[j[0]][j[1]])
        if check_coords[0] == check_coords[1] == check_coords[2] == ' x ':
            return 'x'
        elif check_coords[0] == check_coords[1] == check_coords[2] == ' o ':
            return 'o'

    return False


field = [[' - '] * 3 for i in range(3)]
symb = ' x '

print('   0  1  2')
for i, row in enumerate(field):
    print(i, ''.join(row))

while True:
    x,y = input_coords()
    step(x,y)
    res = check_win()
    if res:
        print('Выиграл ', res)
        break


