# 1.Создайте список из случайных чисел. Найдите номер его последнего
# локального максимума (локальный максимум — это элемент, который больше
# всех из своих соседей).

import random

some_list = [random.randint(1, 100) for _ in range(10)]
print(some_list)
for i in range(len(some_list) - 2, 0, -1):
    if some_list[i - 1] < some_list[i] > some_list[i + 1]:
        print(i + 1)
        print(some_list[i])
        break
