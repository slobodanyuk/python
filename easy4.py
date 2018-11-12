# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def make_dir(dir_name):
    """
    Функция создает новую папку с заданным именем
    в директории с данным скриптом
    """
    if not dir_name:
        print("Введите название папки")
        return
    try:
        os.mkdir(dir_name)
        print("Папка {} успешно создана".format(dir_name))
    except FileExistsError:
        print("Папка с именем {} уже находится по данному адресу".format(dir_name))


def remove_dir(dir_name):
    """
        Функция удаляет существующую пустую папку с заданным именем
        в директории с данным скриптом
        """
    if not dir_name:
        print("Введите название папки")
        return
    try:
        os.rmdir(dir_name)
        print("Папка {} была удалена".format(dir_name))
    except FileNotFoundError:
        print("Папка с именем {0} не найдена по данному адресу: {1}".format(dir_name, os.getcwd()))

for i in range(1, 10):
    make_dir("dir_" + str(i))
    remove_dir("dir_" + str(i))

print("Готово")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def curfolder():
    """
    Функция отображает названия всех файлов и папок
    в текущем расположении
    """""
     return os.listdir(os.curdir)

print(curfolder())