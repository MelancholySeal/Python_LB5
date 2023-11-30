#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    x = float(input("Введите аргумент функции: "))

    result = 0
    n = 0
    term = x

    while abs(term) > 1e-10:
        result += term
        n += 1
        term = -x**2*(2*n+1)/((2*n+3)**2*(2*n+2))

    print(f"Значение интегрального синуса при аргументе {x}: {result}")
