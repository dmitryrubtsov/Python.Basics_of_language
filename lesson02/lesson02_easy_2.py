'''Задача-2:
Даны два произвольные списка.
Удалите из первого списка элементы, присутствующие во втором списке.'''

list_1 = [i for i in range(20)]
list_2 = [i for i in range(0, 20, 2)]
print(f'list 1: {list_1}')
print(f'list 2: {list_2}')

for i in list_2:
    list_1.remove(i)
print(f'new list 1: {list_1}')
