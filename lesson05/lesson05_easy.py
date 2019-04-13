'''Задача-1:
Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
из которой запущен данный скрипт.
И второй скрипт, удаляющий эти папки.

Задача-2:
Напишите скрипт, отображающий папки текущей директории.

Задача-3:
Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.'''

import os
import shutil


def mkdir(dirname):
    '''Create the DIRECTORY'''

    path = os.path.join(os.getcwd(), dirname)

    try:
        os.mkdir(path)
        print(f'Директория {dirname} создана')
    except FileExistsError:
        print(f'Директория {dirname} уже существует')


def rm(dirname):
    '''Delete a directory DIRNAME.'''

    path = os.path.join(os.getcwd(), dirname)

    try:
        os.rmdir(path)
        if not os.path.isdir(path):
            print(f'Папка {dirname} успешно удалена.')
    except FileNotFoundError:
        print(f'Папка {dirname} не найдена.')


def lsdir(path):
    '''List of folders in the current directory'''

    list_dir = [dir for dir in os.listdir(path) if os.path.isdir(dir)]
    list_dir.sort()
    print(*list_dir)


def lsdir2(path):
    '''List of folders and sub folders in the current directory'''

    for _, dirs, _ in os.walk(path):
        dirs.sort()
        print(*dirs)


def copyfile(filename):
    '''Copy files filename to filename.copy'''

    newfile = filename + '.copy'

    shutil.copy(filename, newfile)
    if os.path.isfile(newfile):
        print('Копия файла создана')


if __name__ == '__main__':

    # Задача 1

    for i in range(1, 10):
        dirname = 'dir_' + str(i)
        mkdir(dirname)

    for i in range(1, 10):
        dirname = 'dir_' + str(i)
        rm(dirname)

    # Задача 2

    ls_path = os.getcwd()
    lsdir(ls_path)
    lsdir2(ls_path)

    # Задача 3

    copyfile(__file__)
