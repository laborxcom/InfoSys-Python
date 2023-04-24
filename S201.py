#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Программа должна спросить у пользователя его имя
и поприветствовать пользователя. Она должна написать:
До          11:00 ---> Доброе утро, Ольга!
После       16:00 ---> Добрый вечер, Ольга!
В остальное время ---> Добрый день, Ольга!
Д/З Добавить приветсвие ночью с 01:00 до 03:59
                  ---> Доброй ночи, Ольга!
'''
from datetime import datetime as dt
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# Это моё примечание
t = dt.now()
h = t.hour
m = t.minute
tt = t.time

print(tt)

nam = input('Введите Ваше имя: ')

#if (h > 0 and h < 3) or ((h = 3) and (m < 59)) :
#    print(f'Доброй ночи, {nam}!')
#elif (h > 4 or ( h =3 and m >= 59)) and h < 11:
if h< 11:
    print(f'Доброе утро, {nam}!')
elif h >= 16:
    print(f'Добрый вечер, {nam}!')
else:
    print(f'Добрый день, {nam}!')

print(f'Сегодня {t:%d %B %Y (%A)}')
print(f'Текущее время {t:%H:%M:%S}')

print('END')
