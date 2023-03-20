# 3.Создайте список из случайных чисел. Найдите второй максимум.

import random

some_list = list(set([random.randint(1, 32) for _ in range(10)]))
print(some_list)
first_max = some_list[0]
second_max = some_list[1]
for i in some_list:
    if i > first_max:
        second_max = first_max
        first_max = i
    elif i > second_max and i != first_max:
        second_max = i
print(second_max)
