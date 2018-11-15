# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import easy5

print("Добро пожаловать в утилиту для работы с папками")

print("Мои возможности:", '\n',
      "1. Перейти в папку", '\n',
      "2. Просмотреть содержимое текущей папки", '\n',
      "3. Удалить папку", '\n',
      "4. Создать папку", '\n',
      "5. Завершить работу утилиты")

answer = input(int("Введите номер задачи"))
while answer != 5:
    if answer == 1:
        fname = input("Введите название папки: ")
        easy5.chn_dir(fname)
    elif answer == 2:
        print(easy5.curfolder())
    elif answer == 3:
        fname = input("Введите название папки: ")
        easy5.remove_dir(fname)
    elif answer == 4:
        fname = input("Введите название папки: ")
        easy5.make_dir(fname)