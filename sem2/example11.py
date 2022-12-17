# Задача №11
# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n,
# что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

# Input:     5
# Output:  6
def fibonache(n):
    # 0 1 1 2 3 5 8 13
    if n == 0:
        return 1
    if n == 1:
        return 2, 3
    number0 = 0
    number1 = 1
    count = 2
    while n >= number1:
        if n == number1:
            return count
        temp = number1
        number1 += number0
        number0 = temp
        count += 1
    return -1

n = int(input('введите число: '))
print(fibonache(n))