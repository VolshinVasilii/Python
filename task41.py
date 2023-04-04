"""Дан массив, состоящий из целых чисел. Напишите программу, которая
в данном массиве определит количество элементов, у которых два соседних и,
при этом, оба соседних элемента меньше данного. Сначала вводится число
N — количество элементов в массиве Далее записаны N чисел — элементы
массива. Массив состоит из целых чисел."""


def count_correct_max(arr: list):
    count = 0
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            count += 1
    return count

array_len = int(input("Введите длину массива: "))
array = []
for i in range(array_len):
    array.append(input(f"Введите {i + 1}-й элемент массива: "))

print(array)
print(count_correct_max(array))