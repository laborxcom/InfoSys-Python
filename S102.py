#!/usr/bin/env python3
# -*- coding: utf-8 -*-

YourName = input("Введите Ваше имя: ")
CurYear = input(YourName + ', какой сейчас год? ')
CurYear = int(CurYear)
YearsOld = int(input(YourName + ", сколько Вам лет? "))
FutureYears = CurYear + YearsOld
print(YourName + ', в ' + str(FutureYears) + ' Вам будет ' \
               + str(2*YearsOld) + ' лет.')
