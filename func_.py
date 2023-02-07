def is_digit(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def Number(text):
    number = input(f'{text}')
    while(not is_digit(number)):
        number = input('ОШИБКА. Попробуйте снова: ')
    return int(number)

def open_file(file_name: str):
    with open('data.txt', 'r', encoding='utf-8', ) as datafile:
        result = datafile.read().strip().split('\n')
    return result