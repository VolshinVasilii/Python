# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна
# числу m и наоборот. Например, 220 и 284 – дружественные числа. По
# данному числу k выведите все пары дружественных чисел, каждое из
# которых не превосходит k. Программа получает на вход одно натуральное
# число k, не превосходящее 10**5. Программа должна вывести все пары
# дружественных чисел, каждое из которых не превосходит k. Пары необходимо
# выводить по одной в строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую пару не дает).

def sum_of_divisors(k: int):
    summa = 0
    for i in range(1, k // 2 + 1):
        if k % i == 0:
            summa += i
    return summa


def friendly_numbers(k: int):
    used_numbers = set()
    for i in range(1, k + 1):
        sum_temp_num = sum_of_divisors(i)
        sum2 = sum_of_divisors(sum_temp_num)
        if sum2 == i and sum_temp_num != i and i not in used_numbers and sum_temp_num not in used_numbers:
            print(sum_temp_num, i)
            used_numbers.add(i)


inp_k = int(input("Введите число k: "))

friendly_numbers(inp_k)
