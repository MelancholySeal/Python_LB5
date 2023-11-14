#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = int(input("Введите возраст (n > 100): "))

    if n % 10 == 1 and n % 100 != 11:
        print(f"Мне {n} год.")
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        print(f"Мне {n} года.")
    else:
        print(f"Мне {n} лет.")

