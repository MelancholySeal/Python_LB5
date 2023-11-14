#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def factorial(n):
    return math.factorial(n)

def integral_sin(x, e):
    result = 0
    n = 0
    term = x
    while abs(term) > e:
        result += term
        n += 1
        term = (-1) ** n * (x ** (2 * n + 1)) / (factorial(2 * n + 1))
    return result

if __name__ == '__main__':
    x = float(input("Введите аргумент функции: "))

    e = 1e-10
    result = integral_sin(x, e)

    print(f"Значение интегрального синуса при аргументе {x} с точностью e={e}: {result}")
