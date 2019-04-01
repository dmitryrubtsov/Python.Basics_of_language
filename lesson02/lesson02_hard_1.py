'''Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
вычислите и выведите y'''

import re

equal = input('Введите уравнение прямой y = kx + b: ')
user_x = float(input('Введите x: '))

regex = r"(\d*)x.(\d*)"
matches = re.finditer(regex, equal, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    k = int(match.group(1))
    b = int(match.group(2))

print(f'Для уравнения {equal} при x = {user_x} y = {user_x * k + b}')
