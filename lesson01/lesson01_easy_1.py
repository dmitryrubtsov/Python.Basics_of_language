'''Задача-1: поработайте с переменными, создайте несколько, выведите на экран,
запросите от пользователя и сохраните в переменную, выведите на экран'''

var_int = 10
print(f'У "{var_int}" тип {type(var_int)}')

var_float = 10.0
print(f'У "{var_float}" тип {type(var_float)}')

var_str = 'Текстовая строка'
print(f'У "{var_str}" тип {type(var_str)}')

var_tuple = ('One', 'Two', ('tuple in tuple', 'some text'))
print(f'У "{var_tuple}" тип {type(var_tuple)}')

var_list = ['One', ('tuple in list', ), ['list in list']]
print(f'У "{var_list}" тип {type(var_list)}')

var_dict = {
    1: 'One',
    'two': ['list in dict'],
    ('tuple as key', ): ('tuple in dict', ),
    'dict': {'dict in dict'}
}
print(f'У {var_dict} тип {type(var_dict)}')

var_user = input('Введите что-нибудь: ')
print(f'Вы ввели {var_user}')
