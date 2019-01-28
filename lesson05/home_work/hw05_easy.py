# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys

# dir_name = 'dir_'

i = 0
current_dir = os.getcwd()
dir_list = []  # /  directories list, 0 member is parents dir
while i < 9:
    i += 1
    dir_name = 'dir_' + str(i)
    new_dir = os.path.join(current_dir, dir_name)
    try:
        os.mkdir(new_dir)
        print("Каталог {} создан".format(new_dir))
    except OSError:
        print("Каталог {} уже существует. Ошибка создания каталога".format(new_dir))
    dir_list.append(dir_name)
print(dir_list)

# for x in dir_list:
#     os.rmdir(x)
#     print("Каталог {} удалён".format(x))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
current_dir = os.getcwd()
dir_list = os.listdir(path='.')
files_list = []
for x in dir_list:
    try:
        os.chdir(x)
        os.chdir('..')
    except NotADirectoryError:
        files_list.append(x)
directories = []
for x in dir_list:
    if x in files_list:
        pass
    else:
        directories.append(x)
print("Список подкаталогов в каталоге " + current_dir)
for x in directories:
    print(x)
# print(os.listdir(path='.'))
# print(dir_list)
# print(files_list)
# print(directories)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
file_path = sys.argv
os.system(command=copy)
print(file_path[1])