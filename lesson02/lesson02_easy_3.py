'''Задача-3:
Дан произвольный список из целых чисел.
Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на
два.'''
list_1 = [i for i in range(20)]
list_2 = []
for i in list_1:
    if i % 2 == 0:
        list_2.append(i / 4)
    else:
        list_2.append(i * 2)
print(f'list 1: {list_1}')
print(f'list 2: {list_2}')