# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия,
# имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

fileName = 'tel.txt'

def writeFile(file_name):               
    '''Добавление новой записи'''
    with open(fileName, 'a') as data:
        print('Введите ФИО и телефон именно в таком порядке')
        data.writelines('\n')
        item = ''
        for _ in range(4):
            item += input('>: ')
            item += ','
        data.writelines(item[:-1])

def readFile(file_name): 
    result = []
    with open(fileName, 'r+') as data:
        for line in data:
            result.append(line.split(','))
        return result

def findUser():
    fragment = input('Введите поисковый запрос: ')      #Нийти запись по части имени или телефона. надо разобраться с переносами строк
    with open(fileName, 'r') as userList:
        print(userList)
        for user in userList:
            if fragment in user:
                print(user[0],user[1],user[2],'  -  ',user[3])

def showAllUser():
    with open(fileName, 'r') as datafile:
        for line in datafile:
            newline = line.strip('\n').split(',')
            print('{} {} {}  -  {}'.format(newline[0], newline[1], newline[2], newline[3]))


def deletUser():
    print()

def changePhoneNumber():
    print()

# print(readFile(fileName))
# fragment = input()
# findUser(readFile(fileName), fragment)
# showAllUser(fileName)
# writeFile(fileName)

if __name__ == "__main__":
    # основной блок
    menu = (f"Введите команду\n"
            "1 - Показать все записи\n"
            "2 - Найти запись по части имени или телефону\n"
            "3 - Добавить новый контакт\n"
            '4 - Удалить контакт\n'
            '5 - Изменить номер телефона у контакта\n'
            "6 - Выход\n")
    while True:
        print(menu)
        answer = input(">:")
        match answer:
            case "1":
                # Показать все записи
                showAllUser()

            case "2":
                # Найти запись по вхождению частей имени
                findUser()

            case "3":
                # Добавить новый контакт
                writeFile()

            case "4":
                # удаление данных
                deletUser()

            case "5":
                # удаление данных
                deletUser()    

            case "6":
                # выход
                exit(0)