# Улитка ползет по столбу высотой 12 м, днем на 2м вверх и ночью на 1м вниз.
# На какой день она окажется на вершине"

v = 2
v1 = 1
s = 12
s1 = 0
d = 0
while s1 < s:
    s1 = s1 + v
    d += 1
    if s1 >= s:
        break
s1 = s1 - v1
print(d)

def snail(height, speed_down=1,speed_up=2):
    first_height = height
    day=0
    height_old=height
    while(True):
        day+=1
        height-=speed_up
        if height<=0: return day
        height+=speed_down
        if height>first_height or height==height_old:
            print('Улитка никогда не заползет на столб')
            return None

print(snail(12,1,4))