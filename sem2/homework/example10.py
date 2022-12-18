# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random
def randBinar(n):
    arr = []
    for item in range(n):
        arr.append(random.randint(0, 1))
    return arr

def minFlip(arr):
    zero = one = 0
    for i in arr:
        if i == 0:
            zero +=1
        else:
            one +=1
    if one < zero:
        return one
    else: return zero
    
n = int(input('введите число монеток: '))
coins = randBinar(n)
print(coins)
print('Нужно перевернуть всего', minFlip(coins), 'монеток')