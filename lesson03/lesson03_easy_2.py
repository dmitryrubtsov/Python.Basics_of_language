'''Задание - 2
Создайте функцию, принимающую на вход 3 числа, и возвращающую
наибольшее из них.'''


def max_number(*args):
    '''numbers (int/float) --> max (int/float)'''

    max_num = 0
    for arg in args:
        if arg > max_num:
            max_num = arg
    return max_num


print(max_number(10, 11, 23, 42, 10.5, 50.5))
