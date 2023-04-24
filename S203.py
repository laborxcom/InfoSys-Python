#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Пользователь вводит три целых числа.
Необходимо вывести минимальное из них'''
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
print(a, b, c)

if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)

print('END')
