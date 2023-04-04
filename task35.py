# Напишите функцию, которая принимает одно число и проверяет,
# является ли оно простым

def simple_number(n):
    if n != 2 and n % 2 == 0:
        return False
    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            return False
    return True

input_number = int(input("Введите число для проверки является ли оно простым: "))
print(simple_number(input_number))