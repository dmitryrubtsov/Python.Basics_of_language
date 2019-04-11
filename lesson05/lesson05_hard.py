'''Задание-1:
Доработайте реализацию программы из примера examples/5_with_args.py,
добавив реализацию следующих команд (переданных в качестве аргументов):
  cp <file_name> - создает копию указанного файла
  rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
  cd <full_path or relative_path> - меняет текущую директорию на указанную
  ls - отображение полного пути текущей директории
путь считать абсолютным (full_path) -
в Linux начинается с /, в Windows с имени диска,
все остальные пути считать относительными.

Важно! Все операции должны выполняться в той директории, в который вы
находитесь.
Исходной директорией считать ту, в которой был запущен скрипт.

P.S. По возможности, сделайте кросс-платформенную реализацию.'''


import os
import shutil
import sys

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <dir_name> - создание копии файла")
    print("rm <file_name> - удаляет указанный файл ")
    print("cd <full_path or relative_path> - меняет текущую директорию \
на указанную")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def cp_file():
    if not dir_name:
        print("Необходимо указать имя копируемого файла")
        return
    file_path = os.path.join(os.getcwd(), dir_name)
    new_file = file_path + ".copy"
    shutil.copy(file_path, new_file)
    if os.path.isfile(new_file):
        print(f"Копия файла {dir_name} создана")


def rm_file():
    if not dir_name:
        print("Необходимо указать имя копируемого файла")
        return
    file_path = os.path.join(os.getcwd(), dir_name)
    if os.path.exists(file_path):
        answer = input(f"Удалить файл {dir_name} [Y/N] ").lower()
        print(answer)
        if answer == "y":
            os.remove(file_path)
            if not os.path.exists(file_path):
                print(f"Файл {dir_name} успешно удалён.")
        else:
            print("Удаление файла отменено.")


def cd_dir():
    '''Странная команда. Смена директории происходит в текущем процессе,
    который сразу и завершается.'''
    if not dir_name:
        print("Необходимо указать директорию.")
        return
    path = os.path.abspath(dir_name)
    os.chdir(path)
    if os.getcwd() == path:
        print(f"Текущая директория изменена на {os.getcwd()}")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp_file,
    "rm": rm_file,
    "cd": cd_dir

}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
