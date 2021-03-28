import  shutil
import os
import zipfile

print('Программа, которая дублирует папку и ее содержимое')

folder = input('Введите название папки для бекапа')
file = input('Введите название файла, который нужно откопировать')

os.mkdir(folder)

shutil.copy(file, folder)
zipfile.ZipFile(folder)
