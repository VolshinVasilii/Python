# 25. Напишите программу, которая принимает на вход строку,
# и отслеживает количество повторов каждого символа.


some_string = input("Введите что-нибудь: ")
some_dict = {}
for i in some_string:
    if i in some_dict:
        some_dict[i] += 1
    else:
        some_dict[i] = 1
print(some_dict)
