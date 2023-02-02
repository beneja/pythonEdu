import random

def showMatrix():
    return f'{matrix[0]} {matrix[1]} {matrix[2]} \n{matrix[3]} {matrix[4]} {matrix[5]} \n{matrix[6]} {matrix[7]} {matrix[8]}\n'

def chekWin():
    if matrix[0] == matrix[1] == matrix[2]:
        print(f'Победили {matrix[0]}')
        return 1
    elif matrix[3] == matrix[4] == matrix[5]:
        print(f'Победили {matrix[3]}')
        return 1
    elif matrix[6] == matrix[7] == matrix[8]:
        print(f'Победили {matrix[6]}')
        return 1
    elif matrix[0] == matrix[3] == matrix[6]:
        print(f'Победили {matrix[0]}')
        return 1
    elif matrix[1] == matrix[4] == matrix[7]:
        print(f'Победили {matrix[1]}')
        return 1
    elif matrix[2] == matrix[6] == matrix[8]:
        print(f'Победили {matrix[2]}')
        return 1
    elif matrix[0] == matrix[4] == matrix[8]:
        print(f'Победили {matrix[0]}')
        return 1
    elif matrix[2] == matrix[4] == matrix[6]:
        print(f'Победили {matrix[2]}')
        return 1
    else: return 0

def player():
    while True:
        try:
            number = int(input('Введите номер ячейки чтобы поставить крестик: '))
            if (matrix[number - 1] != 'X') and (matrix[number - 1] != 'O'):
                matrix[number - 1] = 'X'
                break
            else:
                print('Неверный ввод. Ячейка занята')
        except:
            print('Неверный ввод')

def comp(matrix):
    for i in range(0, len(matrix)):
        if matrix[i] != 'X' and matrix[i] != 'O':
            matrix[i] = 'O'
            return

matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(showMatrix())
while True:

    player()
    print(showMatrix())
    if chekWin() == 1:
        break
    comp(matrix)
    print(f'ход компьютера\n{showMatrix()}')
    if chekWin() == 1:
        break