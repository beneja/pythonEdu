# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
# орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные
# спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий
# длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары
# чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины
# полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет
# найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10
from math import pi

# S=pi*a*b
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


def find_farthest_orbit(list_of_orbits):
    s_max = 0
    index = 0
    list_s = []

    def sqare(a, b):
        return pi * a * b

    for i in range(len(list_of_orbits)):
        x = list_of_orbits[i][0]
        y = list_of_orbits[i][1]
        if x != y:
            if sqare(x, y) > s_max:
                s_max = sqare(x, y)
                index = i
        list_s.append(pi * list_of_orbits[i][0] * list_of_orbits[i][1])

    return [list_of_orbits[index], s_max]


print(find_farthest_orbit(orbits))

def find_farthest_orbit1(list_of_orbits):
    list_of_elliptical_orbits = [i for i in list_of_orbits if i[0] != i[1]]
    list_of_areas = [(pi * i[0] * i[1]) for i in list_of_elliptical_orbits]
    max_area_index = list_of_areas.index(max(list_of_areas))
    return list_of_elliptical_orbits[max_area_index]
    
print(find_farthest_orbit1(orbits))