#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = float(input('Введите первый катет: '))
b = float(input('Введите второй катет: '))
s = a * b / 2
print(a, b, s)
# Очень древний способ печати
print('Площадь с %7.3f и %7.3f равна %10.4f' % (a, b, s))

print('END')