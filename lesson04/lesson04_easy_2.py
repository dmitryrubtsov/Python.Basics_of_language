'''Задание-2: Даны два списка фруктов. Получить список фруктов, присутствующих
в обоих исходных списках.'''


list_1 = ['киви', 'апельсин', 'яблоко', 'мандарин', 'груша', 'ананас']
list_2 = ['яблоко', 'дыня', 'арбуз', 'апельсин', 'клюква', 'гранат', 'черника']

set_1 = set(list_1)
set_2 = set(list_2)
print(list_1)
print(list_2)
print(set_1 ^ set_2)
