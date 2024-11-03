from os import *
import time

directory = r'C:\Code and WSs\PyCharm Python\pythonProject\urban_homeworks'
for root, dirs, files in walk(directory): #Не совсем понятно, для чего dirs
    for file in files:
        filepath = path.join(root)
        filetime = path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%y %H:%M", time.localtime(filetime))
        filesize = path.getsize(filepath)
        parent_dir = path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')