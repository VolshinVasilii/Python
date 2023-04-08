def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        print('Вот такой у тебя телефонный справочник:')
        print(f.read())


def add_data() -> None:
    '''Добавляет информацию в справочник'''
    fio = input('Введи Ф.И.О.: ')
    tel_number = input('Введи номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'{fio} | {tel_number}\n')
    print('Добавил, братишка, красаучик!')


def find_data() -> None:
    '''осуществляет поиск из справочника'''
    data = input('Введи, что будем искать: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    if len(search(tel_book, data)) > 0:
        print('Смотри, что нашел:')
        print(search(tel_book, data))
    else:
        print('Ничего не нашел')


def search(book: str, info: str) -> str:
    '''Находит в строке записи по определенному критерию поиска'''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])


def return_of_str(b: str) -> str:
    '''Возвращает строку на выбор'''
    if len(b.split('\n')) > 1:
        num = list(enumerate(b.split('\n')))
        str_num = int(input('Введи, номер строки: '))
        for i in enumerate(b.split('\n')):
            if i[0] == str_num - 1:
                return i[1]
    else:
        return b


def change_data() -> None:
    '''Осуществляет замену одного элемента в справочнике'''
    data = input('Введи, что будем менять: ')
    with open('book.txt', 'r', encoding='utf-8', newline='') as f:
        tel_book = f.read()
    tb = tel_book.split('\n')
    b = search(tel_book, data)
    if len(b) > 0:
        print('Смотри, что нашел:')
        print(b)
        res = return_of_str(b)
        tb[tb.index(res)] = edited(res)
        result = '\n'.join(tb)
        with open('book.txt', 'w', encoding='utf-8', newline='') as f:
            f.write(result)
        print('Замена прошла успешно!')
    else:
        print('Ничего не нашел')


def edited(text: str) -> str:
    fio = input('Введи Ф.И.О. для изменения: ')
    num = input('Введи номер телефона для изменения: ')
    if len(fio) == 0:
        fio = (text.split(' | '))[0]
    if len(num) == 0:
        num = (text.split(' | '))[1]
    return f'{fio} | {num}'


def delete_data() -> None:
    '''Осущестляет удаление одной записи справочника'''
    with open('book.txt', 'r', encoding='utf-8', newline='') as f:
        tel_book = f.read()
    print(tel_book)
    tb = tel_book.split('\n')
    res = return_of_str(tel_book)
    print('Строка удалена')
    tb.pop(tb.index(res))
    result = '\n'.join(tb)
    with open('book.txt', 'w', encoding='utf-8', newline='') as f:
        f.write(result)

