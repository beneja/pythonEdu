# Задача №9. 
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input:       5
# Output:    120
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n-=1
    return result

n = int(input('введите число: '))
print(factorial(n))