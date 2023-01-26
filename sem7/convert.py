import function as fn

def xml(data):
    xml = '<xml>\n'
    for item in data:
        for element in item:
            xml += '    <name unit = "text">{}</name>.\n'.format(element)
    xml += '</xml>'
    with open('data.xml', 'w') as page:
        page.write(xml)
    print('data.xml создан')

def html(data):
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    for item in element:
        for element in item:
            html += '   <p {}>data: {}</p>\n'.format(style, element)
    html += '</body>\n</html>'
    with open('index.html', 'w') as page:
        page.write(html)
    print('index.html создан')

    return 
def choise():
    print('Выберите формат:')
    format = input("1 - xml, 2 - html: ")
    print('Выберите объект для конвертации:')
    item = input('1 - автобусы, 2 - водители, 3 - маршруты\n>:')
    if format == '1' and item == "1":
        xml(fn.read_data_from_file('bus.txt'))
    elif format == '1' and item == "2":
        xml(fn.read_data_from_file('driver.txt'))
    elif format == '1' and item == "3":
        xml(fn.read_data_from_file('marshrut.txt'))
    elif format == '2' and item == "1":
        html(fn.read_data_from_file('bus.txt'))
    elif format == '2' and item == "2":
        html(fn.read_data_from_file('driver.txt'))
    elif format == '2' and item == "3":
        html(fn.read_data_from_file('marshrut.txt'))

# element = fn.read_data_from_file('driver.txt')
# print(element)
# style = 'style="font-size:22px;"'
# html1 = '<html>\n <head></head>\n <body>\n'
# for item in element:
#     for element in item:
#         html1 += '   <p {}>data: {}</p>\n'.format(style, element)
# html1 += '</body>\n</html>'
# print(html1)
# with open('index.html', 'w') as page:
#         page.write(html1)

