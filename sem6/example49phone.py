# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия,
# имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

fileName = 'tel.txt'

def writeFile(file_name):
    with open(fileName, 'a') as data:
        for item in range(4):
            item = input('>: ')
            data.writelines(item + ',')

def save_data_to_file(data_to_save):
    '''запись строки данных в конец файла'''
    data_to_save = ",".join(data_to_save) + "\n"
    print(data_to_save)
    with open(fileName, "a", encoding="utf8") as datafile:
        datafile.write(data_to_save)

def add_data():
    '''добавление записи'''
    while True:
        print('Добавление записи(""-выход)>:')
        last_name = input("Фамилия: ")
        if last_name == "":
            return
        first_name = input("Имя: ")
        patronymic = input("Отчество: ")
        phone_number = input("Номер Телефона: ")
        data_to_save = [last_name, first_name, patronymic, phone_number]
        if "" in data_to_save:
            return
        save_data_to_file(data_to_save)


def readFile(file_name):
    result = []
    with open(fileName, 'r+') as data:
        for line in data:
            result.append(line.split(','))
        return result

def findUser(userList, fragment):
    for user in userList:
        if user[1] == fragment:
            print(user[0],user[1],user[2],'  -  ',user[3])

def showAllUser(printdata):
    with open(fileName, 'r') as datafile:
        for line in datafile:
            newline = line.strip('\n').split(',')
            print('{} {} {}  -  {}'.format(newline[0], newline[1], newline[2], newline[3]))



# print(readFile(fileName))
# fragment = input()
# findUser(readFile(fileName), fragment)
# showAllUser(fileName)
writeFile(fileName)
