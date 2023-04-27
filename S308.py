#!/usr/bin/env python3
# -*- coding: utf-8 -*-

t = '''НЕОБХОДИМО НАПЕЧАТАТЬ ВСЕ ГЛАСНЫЕ БУКВЫ ИЗ ДАННОГО ТЕКСТА
независимо от их РЕГИСТРА. Кроме того, нужно подсчитать сколько
и какие гласные буквы в нём встречаются. Итоговый список 
требуется вывести на печать в двух вариантах: 1) по алфавиту,
2) по частоте появления букв. Буква 'а' --> 12 '''
print(t)
wow = 'ёуеыаоэяию'

print(''.join([x for x in t if x.lower() in 'ёуеыаоэяию']))

d = {}
for letter in filter(lambda b: b.lower() in wow, t):
    ln = letter.lower()
    if ln in d:
        d[ln] += 1
    else:
        d[ln] = 1

print(d)
# Д/З: Дописать программу до конца

#=======================================================

print("Гласные буквы по алфавиту:")
for key in sorted(d.keys()):
    print(f"{key}: {d[key]}")

print("Гласные буквы по частоте появления:")
for item in sorted(d.items(), key=lambda x: x[1], reverse=True):
    print(f"{item[0]}---> {item[1]}")


#=======================================================


for b, n in sorted(d.items()):
    print(f"'{b}' --> {n:3}")
print(30 * '*')

for b, n in sorted(d.items(), key=lambda x: x[1], reverse=True):
    print(f"'{b}' --> {n:3}")

#=======================================================
print('\nEND')
