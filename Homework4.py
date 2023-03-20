# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго
# множества. Затем пользователь вводит сами элементы множеств.

import random
first_list = [random.randint(1, 10) for _ in range(10)]
print(first_list)
second_list = [random.randint(1, 10) for _ in range(10)]
print(second_list)
third_list = []
for i in first_list:
    for j in second_list:
        if i == j:
            third_list.append(i)
            break
third_list = list(set(third_list))
# print(sorted(third_list)
for i in range(len(third_list) - 1):
    if third_list[i + 1] < third_list[i]:
        third_list[i], third_list[i + 1] = third_list[i + 1], third_list[i]
print(third_list)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по
# окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и
# нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает
# ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

import random
bush = int(input("Сколько у нас кустов?: "))
some_list = [random.randint(1, 10) for _ in range(bush)]
print(some_list)
summa = 0
max_sum = 0
penultimate_sum = 0
ultimate_sum = 0
lenght = len(some_list)
for i in range(len(some_list) - 3):
    penultimate_sum = some_list[lenght - 2] + some_list[lenght - 1] + some_list[0]
    ultimate_sum = some_list[lenght - 1] + some_list[0] + some_list[1]
    summa = some_list[i] + some_list[i + 1] + some_list[i + 2]
    if summa > max_sum:
        max_sum = summa
    if penultimate_sum > max_sum:
        max_sum = penultimate_sum
    if ultimate_sum > max_sum:
        max_sum = ultimate_sum
print(f"Максимальное количество ягод за один заход: {max_sum}")