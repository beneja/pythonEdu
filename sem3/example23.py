# 23
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2
# пояснение
# (-1 < 5, 2 < 3)
import random
def randArr(n):
    arr = []
    for item in range(n):
        arr.append(random.randint(-5, 5))
    return arr

array = randArr(10)
count = 0
for i in range(1, len(array)):
    if array[i - 1] < array[i]:
        count += 1

print(array)
print(count)

