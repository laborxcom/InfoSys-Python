#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Пользователь вводит два целых числа А и В.
Выведите все числа от А до В включительно в
порядке возрастания, если А < В, или в порядке
убывания в противном случае.'''
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)

if a < b:
    for i in range(a, b + 1):
        print(i, end=' ')
else:
    for i in range(a, b - 1, -1):
        print(i, end=' ')

print('\nEND')
