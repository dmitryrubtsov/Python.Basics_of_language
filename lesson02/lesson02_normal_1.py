'''Задача-1:
Дан список, заполненный произвольными целыми числами, получите новый список,
элементами которого будут квадратные корни элементов исходного списка,
но только если результаты извлечения корня не имеют десятичной части и
если такой корень вообще можно извлечь
Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]'''


import random

def square(n):
    if n > 0:
        for i in range(n+1):
            if i ** 2 == n:
                return i
            elif i ** 2 > n:
                return False
    else:
        return False


list_item = [random.randint(-25, 25) for _ in range(15)]
print(list_item)
list_square = []

for i in list_item:
    if square(i) != False:
        list_square.append(square(i))
print(list_square)
