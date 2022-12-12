value = None
a = 123
b = 1.324
print(type(value))
print(type(a))
print(type(b))
value = 123123
print(type(value))
s = 'hello world' # ковычки заменяемы
print(s) # вывод
print(a, '-', b, '-', s)
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = True
print(f)

# print('Введите a');
# a = int(input())
# print('Введите b');
# b = int(input())
# print(a,' + ', b, ' = ', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text:
    print(c)

text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...