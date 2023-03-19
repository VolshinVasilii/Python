# 21. Напишите программу для печати всех уникальных значений
# в словаре.

input_dict = {}
input_dict_len = int(input("Введите количество элементов в словаре: "))
for _ in range(input_dict_len):
    input_key = input("Введите ключ: ")
    input_value = input("Введите значение для ключа: ")
    input_dict[input_key] = input_value
print(set(input_dict.values()))
