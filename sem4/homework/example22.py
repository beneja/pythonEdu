# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12
import random
def randArr(n):
    arr = []
    for item in range(n):
        arr.append(random.randint(0, n))
    return arr
n = int(input('введите количество элементов первого набора: '))
m = int(input('введите количество элементов первого набора: '))
arrN = randArr(n)
print(arrN)
arrM = randArr(m)
print(arrM)
data = {}
for item in arrN:
    data[item] = None
for item in arrM:
    if item in data:
        data[item] = 1
sorted_data = dict(sorted(data.items()))
result = ''
for i in sorted_data:
    if sorted_data[i] == 1:
        result += str(i) + " "
print(result)