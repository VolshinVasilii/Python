# Дан список интов,повторяющихся элементов в списке нет. Нужно
# преобразовать этo множество в строку, сворачивая соседние по числовому
# ряду числа в диапазоны. Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

import random

def a(list):
    list.append(1.9)
    temp_result = []
    result = []
    for i in range(len(list) - 1):
        if list[i + 1] == list[i] + 1:
            temp_result.append(list[i])
        else:
            if list[i] not in temp_result:
                temp_result.append(list[i])
            result.append(temp_result)
            temp_result = []
    print(result)
    result_str = []
    for i in result:
        if len(i) >= 2:
            result_str.append(f"{i[0]}-{i[-1]}")
        else:
            result_str.append(f"{i[0]}")
    return result_str

input_list = sorted(set([random.randint(1, 10) for _ in range(10)]))

print(input_list)
print(*a(input_list), sep=', ')
