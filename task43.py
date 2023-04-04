# Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента, равные друг другу
# образуют одну пару, которую необходимо посчитать.

import random


def count_pairs(arr: list):
    cnt = 0
    some_dict = {}
    for i in arr:
        if i in some_dict:
            some_dict[i] += 1
        else:
            some_dict[i] = 1
    print(some_dict)
    for i in some_dict.values():
        cnt += i // 2
    return cnt
    # set_arr = set(arr)
    # for i in set_arr:
    #      cnt += arr.count(i) // 2
    # return cnt


array = [random.randint(1, 10) for _ in range(10)]
print(array)
print(count_pairs(array))
