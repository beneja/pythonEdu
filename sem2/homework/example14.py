#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
N = int(input("введите число: "))

number = 2
while number <= N:
    print(number)
    number *= 2
