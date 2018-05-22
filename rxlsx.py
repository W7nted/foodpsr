#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd

try:
    excel_data_file = xlrd.open_workbook('./foodtmp.xlsx')
except IOError as e:
    print(u'Не удалось открыть файл')
    exit()

# Получаем индекс последнего листа
last_sheet = excel_data_file.nsheets

# Открываем последний лист по индексу
sheet = excel_data_file.sheet_by_index(last_sheet - 1)

# Получаем данные из последнего листа
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

# Удаляем пустые значения в списке
vals2 = []
for i in range(len(vals)):
    vals2.append([])
    for el in vals[i]:
        if el != '': vals2[i].append(el)

# Удаляем пустые вложенные списки
vals = [value for value in vals2 if value]

# Удаляем не нужные элементы
# del vals[-3:]
del vals[:1]

# Избавляемся от вложенных списков
vals2 = []
for i in vals:
    for j in i:
        vals2.append(j)
vals = vals2
del vals2

# Создаем списки  по дням
week = ('Вторник', 'Среда', 'Четверг', 'Пятница',)

monday_menu = vals[:vals.index(week[0])]
tuesday_menu = vals[vals.index(week[0]):vals.index(week[1])]
wednesday_menu = vals[vals.index(week[1]):vals.index(week[2])]
thursday_menu = vals[vals.index(week[2]):vals.index(week[3])]
friday_menu =  vals[vals.index(week[3]):]

print(monday_menu)
print(tuesday_menu)
print(wednesday_menu)
print(thursday_menu)
print(friday_menu)

