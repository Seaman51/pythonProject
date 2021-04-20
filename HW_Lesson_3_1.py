"""
Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла,
а затем «выделение» из этого пути имени файла (без расширения).
"""
import os


def find_file(name_file):
    if os.path.exists(name_file):
        path_file = os.path.abspath(name_file)
        name_file = (os.path.basename(path_file).split('.'))[0]
        return name_file
    else:
        return 'Not found'


print(find_file("README.md"))
