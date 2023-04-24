#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = '''В ДАННОМ ТЕКСТЕ БУКВА "Н" ВСТРЕЧАЕТСЯ,
как минимум, два раза. Разверните последовательность
символов, заключённую между первым и последним 
появлением буквы 'н', в противоположном порядке.'''
print(s)
a = s[:s.lower().find('н') + 1]
b = s[s.lower().find('н') + 1:s.lower().rfind('н')]
c = s[s.lower().rfind('н'):]
print(f'\na = >>>{a}<<<')
print(f'\nb = >>>{b}<<<')
print(f'\nc = >>>{c}<<<')
t = a + b[::-1] + c
print(t)


print((v := input(':> '))[:v.lower().find('н') + 1] + v[v.lower().find('н') + 1:v.lower().rfind('н')][::-1] + v[v.lower().rfind('н'):])
