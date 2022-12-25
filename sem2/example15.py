# Задача №15
# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза.
# Все числа натуральные и не превышают 30000.
import random
def arbuzLine(N):
    arbuzes = []
    for _ in range(N):
        arbuzes.append(random.randint(5000, 30000))
    #arbuzes.sort()
    print(arbuzes)
    
    min = max = arbuzes[0]
    for item in arbuzes :
        if min > item : min = item
        elif max < item : max = item 
    return min, max

n = int(input('введите число: '))
print(arbuzLine(n))