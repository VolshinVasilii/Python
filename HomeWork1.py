# Задача 2: Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трехзначное число: "))
number = input("Введите трехзначное число: ")
# first = number // 100
first = int(number[0])
# second = number // 10 % 10
second = int(number[1])
# third = number % 10
third = int(number[2])
sum = first + second + third
print(f"{number} -> {sum} ({first} + {second} + {third})")


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

number = int(input("Введите сколько журавликов сделали ребята вместе: "))
if number % 6 == 0:
    print(f"{number} -> {round(number / 6)} {round(number / 6 * 4)} {round(number / 6)}")
else:
    print("Ну так не работает, друг")


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

number = input("Введите номер билета: ")
if int(number[0]) + int(number[1]) + int(number[2]) == int(number[3]) + int(number[4]) + int(number[5]):
    print("Поздравляю, Ваш билет - счастливый")
else:
    print("Не сегодня, друг")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите длину шоколады (в дольках): "))
m = int(input("Введите ширину шоколады (в дольках): "))
k = int(input("Введите сколько долек нужно отломить от шоколады: "))
if k < n * m and (k % m == 0 or k % n == 0):
    print("Такое допускается")
else:
    print("Так сделать не получится")
