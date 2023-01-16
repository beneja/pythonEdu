# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое
# значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для
# разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
# вывод same
def same_by(f, list_num):
    return len(set(map(f, list_num))) == 1
values = [0, 2, 10, 6, 6]
print(values)
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')