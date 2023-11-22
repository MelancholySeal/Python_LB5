#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

x = float(input("Введите аргумент функции: "))

result = 0
n = 0
term = x

while abs(term) > 1e-10:
    result += term
    n += 1
    term = (-1) ** n * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)

print(f"Значение интегрального синуса при аргументе {x} с точностью e=1e-10: {result}")