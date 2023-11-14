#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    for number in range(100, 1000):
        digits = list(map(int, str(number)))

        digit_sum = sum(digits)
        digit_product = 1
        for digit in digits:
            digit_product *= digit
            
        if digit_sum == digit_product:
            print(number)

