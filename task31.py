# 1. Последовательностью Фибоначчи называется последовательность
# чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# 0, 1, 1, 2, 3, 5, 8, 13...

def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)
print(fibo(8))


def fibo_iteration(n):
    first = 0
    second = 1
    if n == 1:
        return first
    if n == 2:
        return second
    count = 2
    while n != count:
        third = first + second
        first = second
        second = third
        count += 1
    return third
print(fibo_iteration(8))

