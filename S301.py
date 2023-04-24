#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Пользователь вводит строку, сотоящую из двух слов,
разделённых ровно одним пробелом. 
Поменяйте эти слова местами.'''
s = input(':> ').strip()
print(f'>>>{s}<<<')
first_word = s[:s.find(' ')]
second_word = s[s.find(' ') + 1:]
t = second_word + ' ' + first_word
print(t)

print('END')
