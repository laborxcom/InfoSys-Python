#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os.path import join, abspath
from re import findall

data_path = join('..', 'Data', 'voyna-i-mir-tom-1.txt')
print(data_path)
data_path = abspath(data_path)
print(data_path)

bslov = {}
with open(data_path, mode='rt', encoding='cp1251') as src:
    for line in src:
        ln = line.strip().lower()
        ln = findall(r'\w{6,}', ln)
        for st in ln:
            bslov[st] = bslov.get(st, 0) + 1
spis = sorted(bslov.items(),
              key=lambda x: x[1],
              reverse=True
              )
write_path = abspath(join('..', 'Data', 'vse_slova.txt'))
print(write_path)

with open(write_path, mode='wt', encoding='utf-8') as dst:
    for s, n in spis:
        print(f'{s:25} ---> {n:4}', file=dst)

print('END')
