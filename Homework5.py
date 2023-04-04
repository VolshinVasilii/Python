# Дана строка (возможно, пустая),состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28 И сгенерирует ошибку,
# если на вход пришла невалидная строка. Пояснения:Если символ встречается 1 раз,он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений

# some_string = input("Введите что-нибудь: ")
#
#
# def num_of_letters(strng):
#     res_list = []
#     strng += ' '
#     temp_letter = strng[0]
#     count_letter = 1
#     for ind in range(1, len(strng)):
#         if strng[ind] == temp_letter:
#             count_letter += 1
#         else:
#             if count_letter == 1:
#                 res_list.append(f'{temp_letter}')
#             else:
#                 res_list.append(f'{temp_letter}{count_letter}')
#             count_letter = 1
#             temp_letter = strng[ind]
#     print(*res_list, sep='')
#
# num_of_letters(some_string)


# Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по "общим буквам".

# def group_letter(input_list):
#     word_dict = {}
#     for word in input_list:
#         if (frozenset(word), len(word)) not in word_dict:
#             word_dict[(frozenset(word), len(word))] = [word]
#         else:
#             word_dict[(frozenset(word), len(word))].append(word)
#     res_list = []
#     for value in word_dict.values():
#         res_list.append(value)
#     return res_list
# print(group_letter(["eat", "tea", "tan", "ate", "nat", "bat", "batt", "b", "caddsfa"]))
