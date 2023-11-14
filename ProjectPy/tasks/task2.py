#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def determine_jp_year(year):
    colors = ["зеленый", "красный", "желтый", "белый", "черный"]
    animals = ["мыши", "коровы", "тигра", "зайца", "дракона", "змеи", "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"]

    start_year = 1984
    cycle_length = 60

    offset = (year - start_year) % cycle_length

    color_index = (offset // 12) % len(colors)
    animal_index = offset % len(animals)

    jp_year = f"{colors[color_index]} {animals[animal_index]}"
    return jp_year

if __name__ == '__main__':
    year = int(input("Введите год: "))
    jp_year = determine_jp_year(year)
    print(f"{year} - год {jp_year} по японскому календарю.")
