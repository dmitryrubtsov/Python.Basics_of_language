'''Задача-4: Дан список, заполненный произвольными целыми числами.
Получите новый список, элементами которого будут:
а) неповторяющиеся элементы исходного списка:
например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
б) элементы исходного списка, которые не имеют повторений:
например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
'''

list_1 = [1, 2, 4, 5, 6, 2, 5, 2]
list_2a = []
list_2a.extend(list_1)
list_2b = []

for i in list_2a:
    if list_2a.count(i) > 1:
        list_2a.remove(i)
list_2a.sort()

for i in list_1:
    if list_1.count(i) == 1:
        list_2b.append(i)

print(f'Неповторяющиеся элементы исходного списка: {list_2a}')
print(f'Элементы исходного списка, которые не имеют повторений: {list_2b}')

print(f'Неповторяющиеся элементы исходного списка: {set(list_1)}')
