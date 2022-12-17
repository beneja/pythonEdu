def binary_search(list, item):
    low = 0                   #В переменнь1х low и high хранятся границы той части списка,
    high = len(list)-1          #в которой выпоnняется поиск
    while low <= high :         #Пока часть не сократится до одного элемента проверяем средний элемент
        mid = (low + high)
        guess = list[mid]
        print(list[mid])
        if guess == item :      #Нашёл
            return mid
        if guess > item:        #много
            high = mid - 1
        else:                   #мало
            low = mid + 1
    return None
my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => None