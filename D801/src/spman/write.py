#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = [
    'output_simple',
    'output_all',
]

def output_simple(superman):
    v, f = superman
    txt = f'* {f:15} | {v:10.3f} *'
    print(txt)

def output_all(d):
    print('*' * 32)
    print('*     Фамилия     |  Результат *')
    print('*' * 32)
    for x in d:
        output_simple(x)
    print('*' * 32)
    