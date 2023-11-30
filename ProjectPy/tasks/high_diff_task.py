#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    x = float(input("Введите аргумент функции: "))

    result = x
    n = 0
    term = result

    while math.fabs(term) > 1e-10:
        term *= -x ** 2 * (2 * n + 1) / ((2 * n + 3) ** 2 * (2 * n + 2))
        result += term
        n += 1

    print(f"Значение интегрального синуса при аргументе {x}: {result}")