'''Задание-3: Дан список, заполненный произвольными числами. Получить список из
элементов исходного, удовлетворяющих следующим условиям:

Элемент кратен 3
Элемент положительный
Элемент не кратен 4'''


import random


def filter_1(x):
    if x % 3 == 0 and x > 0 and x % 4 != 0:
        return True


orig_list = [random.randint(-100, 100) for _ in range(30)]
print(orig_list)
list_1 = list(filter(filter_1, orig_list))
print(list_1)
