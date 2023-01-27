def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b

def simplification(expression):
    m3 = []
    for i in range(1, len(m) - 1, 2):
        a = int(expression[i - 1])
        b = int(expression[i + 1])
        action = expression[i]
        if m[i] == '*' or m[i] == '/':
            result = calc(a, b, action)
            if i > 2:
                m3.pop()
            m3.append(result)
        else:
            m3.append(action)
            m3.append(b)
    return m3

n = '11 / 1 - 22 * 10 - 14 + 10 * 8 + 7'
m = n.split()
print(m)
if '/' in m or '*' in m:
    m4 = simplification(m)
final_result = int(m4[0])
for i in range(1, len(m4) - 1, 2):
    if m4[i] == '+' or m4[i] == '-':
        final_result = calc(final_result, int(m4[i + 1]), m4[i])
print(final_result)

