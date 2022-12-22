# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое
# необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X,
# выведите наименьший по величине.
# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6
import random
def randArr(n):
    arr = []
    for item in range(n):
        arr.append(random.randint(1, n))
    return arr


def findNearest(array, x):
    diffCurrent = 0
    diffMin = len(array)
    value = 0
    for item in array:
        diffCurrent = abs(item - x)
        if diffMin >= diffCurrent:
            diffMin = diffCurrent
            value = item
    for item in array:
        if item == (x - diffMin):
            value = item
    return value


array = randArr(int(input('Введите количество элементов: ')))
# array = [1, 2, 1, 8, 9, 6, 5, 4, 3, 4, 8]
x = int(input('введите число: '))
k = array.count(x)
for i in range(k):
    array.remove(x)
print(array)
print(findNearest(array, x))
