"""39. Даны два массива чисел. Требуется вывести те элементы первого
массива (в том порядке, в каком они идут в первом массиве), которых нет
во втором массиве. Пользователь вводит число N - количество элементов
в первом массиве, затем N чисел - элементы массива. Затем число M -
количество элементов во втором массиве. Затем элементы второго массива"""

def cross_arrays(inp_arr_1, inp_arr_2):
    second_set = set(inp_arr_2)
    result = []
    for i in inp_arr_1:
        if i not in second_set:
            result.append(i)
    return result

first_array_len = int(input("Введите длину первого массива: "))
first_array = []
for i in range(first_array_len):
    first_array.append(input(f"Введите {i + 1}-й элемент первого массива: "))
second_array_len = int(input("Введите длину второго массива: "))
second_array = []
for i in range(second_array_len):
    second_array.append(input(f"Введите {i + 1}-й элемент второго массива: "))

print(cross_arrays(first_array, second_array))