#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import spman as sp

best = list()

for x in sp.input_all():
    best.append(x)
    best.sort()
    if len(best) > 5:
        del best[-1]
    sp.output_all(best)


print('END')
