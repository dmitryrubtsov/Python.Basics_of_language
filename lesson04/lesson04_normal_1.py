'''Задача - 1 Запросите у пользователя имя, фамилию, email. Теперь необходимо
совершить проверки, имя и фамилия должны иметь заглавные первые буквы. email -
не должен иметь заглавных букв и должен быть в формате: текст в нижнем
регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст,
допускаются цифры, точка, ru или org или com. Например: Пупкин василий -
неверно указано имя, te$T@test.net - неверно указан email (спецсимвол,
заглавная буква, .net), te_4_st@test.com - верно указан.'''

import re

name_patten = r'^[A-ZА-ЯЁ][a-zа-яё]+$'
email_patten = r'^[a-z0-9_]+@[a-z0-9]+.(ru|org|com)$'

while True:
    name = input('Введите имя: ')
    name_matches = re.match(name_patten, name, re.MULTILINE)
    if name_matches is None:
        print('Имя введено не верно. Попробуйте ещё раз.')
    else:
        break

while True:
    last_name = input('Введите фамилию: ')
    last_name_matches = re.match(name_patten, last_name, re.MULTILINE)
    if last_name_matches is None:
        print('Фамилия введена не верно. Попробуйте ещё раз.')
    else:
        break

while True:
    email = input('Введите email: ')
    email_matches = re.match(email_patten, email, re.MULTILINE)
    if email_matches is None:
        print('Email введён не верно. Попробуйте ещё раз.')
    else:
        break
print(name_matches.group(), last_name_matches.group(), email_matches.group())
