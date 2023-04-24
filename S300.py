#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 15
b = 10 + 5

a == b
a is b

import sys
sys.getrefcount(a)


c = 111111
d = 111100 + 11

c == d
c is d
