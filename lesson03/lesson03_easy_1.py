'''Задание - 1
Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
Функция должна возвращать строку вида
"Василий, 21 год(а), проживает в городе Москва"'''


def user_map(name, age, city):
    '''name(str), age(str), city(str) --> str'''

    str_user = f'{name}, {age} год(а), проживает в городе {city}'
    return str_user


print(user_map('Василий', '21', 'Москва'))
