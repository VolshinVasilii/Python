# 19. Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

input_list = []
list_len = int(input("Введите количество элементов в списке: "))
for _ in range(list_len):
    input_list.append(int(input(f"Введите число: ")))
print(input_list)

k = int(input("Введите на сколько элементов сместить последовательность: "))
while k > len(input_list):
    k = k - len(input_list)
print(f"{input_list[-k:] + input_list[:-k]}")
