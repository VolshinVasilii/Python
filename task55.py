# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

import functions

while True:
    print("1. Вывод данных, 2. Добавление, 3. Поиск, 4. Замена, 5. Удаление")
    mode = int(input('Вводи, что будем выполнять: '))
    if mode == 1:
        functions.show_data()
    elif mode == 2:
        functions.add_data()
    elif mode == 3:
        functions.find_data()
    elif mode == 4:
        functions.change_data()
    elif mode == 5:
        functions.delete_data()
    else:
        break




# with open('book.txt', 'w', encoding='utf-8') as f:
#     f.write('фио | номер телефона')
#
# with open('book.txt', 'a', encoding='utf-8') as f:
#     f.write('\nфио1 | номер телефона1')
#
# with open('book.txt', 'r', encoding='utf-8') as f:
#     print(f.read())








