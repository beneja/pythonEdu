# Задача №13
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая
# длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те,
# в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует,
# сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который
# среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу,
# помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел. 
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа
# и лежат в диапазоне от –50 до 50

# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2
import random
n = 20
m = []
count = max = 0
for i in range(0, n):
    random_number = round(random.uniform(-50,50), 0)
    m.append(random_number)
    if m[i] < 0 :
        count = 0
    if m[i] > 0 :
        count += 1
        if max < count :
            max = count


print(m)
print(max)