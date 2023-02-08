from datetime import datetime

birthdays = []

with open('data.txt', 'r', encoding= 'UTF-8') as file:
    for line in file:
        line_date = datetime.strptime(line[:10], "%d.%m.%Y").date()
        newline = line.strip().replace (line[:10], str(line_date))
        birthdays.append(newline)

birthdays_sort = sorted(birthdays, key = lambda x: x[5:10])
# print (birthdays_sort)
todays = datetime.now().timetuple()
year = todays.tm_year
i = 0
for friend in birthdays_sort:
    month, day = int(friend[5:7]) , int(friend[5:7])
    friend_date = datetime(year, month, day).timetuple()
    days_away = friend_date.tm_yday - todays.tm_yday
    friend_age = year - int(friend[:4])
    item = birthdays_sort.pop(i).split()
    birthdays_sort.insert(i, (item[0], item[1], friend_age, days_away))
    i += 1

for f in birthdays_sort:
    if f[3] == 0:
        print('{} СЕГОДНЯ {} лет!'.format(f[1],f[2]))  
    elif f[3] > 0:
        print('{} будет {} лет через {} дней'.format(f[1],f[2],f[3]))
    else: 
        print('{} день варенья был {} дня назад. Исполнилось {} лет'.format(f[1],f[3],f[2]))

# print(birthdays_sort)