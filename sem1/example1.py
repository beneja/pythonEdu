# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать
# марщрут длинной m километров? Прирешении этой задачи нельзя пользоваться
# условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

n = int(input('введите проезжаемое за день расстояние: '))
m = int(input('введите длинну пути: '))
t = (m + n - 1) // n
print(t)
