#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from decimal import Decimal

__all__ = [
    'input_simple',
    'input_all',
]

TOCHNOST = Decimal('0.001')

def input_simple():
    res = input('Res: ')
    res = Decimal(res).quantize(TOCHNOST)
    fam = input('Fam: ')
    return res, fam

def input_all():
    while True:
        yield input_simple()
