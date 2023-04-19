#!/usr/bin/env python3
# -*- coding: utf-8 -*-

nam = input("Введите Ваше имя: ")
god = input(nam + ', какой сейчас год? ')
god = int(god)
let = int(input(nam + ", сколько Вам лет? "))
ngod = god + let
print(nam + ', в ' + str(ngod) + ' Вам будет ' \
               + str(2*let) + ' лет.')
               