# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число,
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2
import random
def randArr(n):
    arr = []
    for item in range(n):
        arr.append(random.randint(1, n//2))
    return arr

def findNumber(array1, X):
    count = 0
    for i in array1:
        if i == X:
            count += 1
    return count
array = randArr(int(input('Введите размер массива: ')))
x = int(input('Введите число для поиска: '))
print(array)
print(x,' встречается ',findNumber(array, x), ' раз')