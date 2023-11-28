#!/usr/bin/env python3
# -*- coding: utf-8 -*-

colors = ["зеленый", "красный", "желтый", "белый", "черный"]
animals = ["мыши", "коровы", "тигра", "зайца", "дракона", "змеи", "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"]

start_year = 1984
cycle_length = 60

year = int(input("Введите год: "))
offset = (year - start_year) % cycle_length

color_index = (offset // 12) % len(colors)
animal_index = offset % len(animals)

jp_year = f"{colors[color_index]} {animals[animal_index]}"
print(f"{year} - год {jp_year} по японскому календарю.")
