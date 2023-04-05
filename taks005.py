# Если ты много лет подряд был воином
# Белой розы, если ты не раз участвовал в
# кровопролитных битвах между индейцами и бледнолицыми,
# если ты, наконец, был разведчиком союзников во второй
# мировой войне, то ты научился двум вещам: ничему не
# удивляться и уметь молчать, когда надо.
# Напишите программу, которая найдет отличия между
# индейцами и бледнолицыми (или Белой розой и Красной
# розой, кто их разберет!).
# Из каждых двух наборов целых чисел выбрать общие,
# оканчивающиеся на 1 или 3, без повторений. Вывести
# в порядке убывания через &, окруженный пробелами.
# Формат ввода
# Вводится число n – количество наборов из двух
# строк, в которых целые числа записаны через пробел.
# Затем 2 * n строк с целыми числами.
# Формат вывода
# Вывести n строк, в которых записаны определенные по
# указанному правилу числа через &, окруженный пробелами
# Ввод
# 3
# 9 28 21 23 12 41
# 6 21 18 26 41 18 23 53
# 18 4 25 31 15 20 31 1
# 2 13 10 28 12
# 10 31 23 13 121 17 9 18
# 31 9 3 10 121 4 14 21
#
# вывод
# 41 & 23 & 21
# 121 & 31


# input_str_list = {}
# input_len_str_list = int(input("Введите количество пар строк: "))
#
# for i in range(input_len_str_list):
#     input_str_list[i] = []
#     input_str_list[i].append(list(map(lambda x: int(x), input("Введите числа разделенными пробелами: ").split())))
#     input_str_list[i].append(list(map(lambda x: int(x), input("Введите числа разделенными пробелами: ").split())))
# print(input_str_list)
# result = {}
#



n = int(input())

# some_list = [[i for i in input().split() if i[-1] in ('1', '3')] for _ in range(2 * n)]

some_list = []
for _ in range(2 * n):
    temp_list = []
    for i in input().split():
        if i[-1] in ('1', '3'):
            temp_list.append(i)
    some_list.append(temp_list)

print(some_list)
for ind in range(0, len(some_list) - 1, 2):
    res = list(set(some_list[ind]).intersection(set(some_list[ind + 1])))
    res = list(map(int, res))
    print(*sorted(res, reverse=True), sep=' & ')
