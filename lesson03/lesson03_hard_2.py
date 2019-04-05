'''Задание - 2
Давайте усложним предыдущее задание, измените сущности, добавив новый
параметр - armor = 1.2
Теперь надо добавить функцию, которая будет вычислять и возвращать полученный
урон по формуле damage / armor
Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет
урон по отношению к броне.

Сохраните эти сущности, полностью, каждую в свой файл,
в качестве названия для файла использовать name, расширение .txt
Напишите функцию, которая будет считывать файл игрока и его врага, получать
оттуда данные, и записывать их в словари, после чего происходит запуск игровой
сессии, где сущностям поочередно наносится урон, пока у одного из них health
не станет меньше или равен 0.
После чего на экран должно быть выведено имя победителя, и количество
оставшихся единиц здоровья.'''


import os
import pickle
import random


MIN_HEALTH = 40
MAX_HEALTH = 200
MIN_DAMAGE = 0.5
MAX_DAMAGE = 2.5
MIN_ARMOR = 1.0
MAX_ARMOR = 2.5


def is_file_txt(file_name):
    ''' Проверяет наличие файла user.txt, если нет создаёт его.
    Формат файла текст.
    Генерирует health, damage, armor.
    str --> True
    '''

    user_skills = {}

    if not os.path.exists(file_name):
        user_skills['name'] = file_name.split('.')[0]
        user_skills['health'] = random.randint(MIN_HEALTH, MAX_HEALTH)
        user_skills['damage'] = round(
            random.uniform(MIN_DAMAGE, MAX_DAMAGE), 1
        )
        user_skills['armor'] = round(random.uniform(MIN_ARMOR, MAX_ARMOR), 1)
        with open(file_name, 'w') as file:
            for key, item in user_skills.items():
                file.write(f'{key}:{item}\n')
    return True


def init_txt(user):
    '''
    создаёт их. Загружает сущности из файла в словарь и возвращает его.
    '''
    file_name = user + '.txt'
    user_skills = {}

    if is_file_txt(file_name):
        with open(file_name) as file:
            for line in file.readlines():
                key, value = line.strip().split(':')
                if value.isalpha():
                    user_skills[key] = value
                else:
                    user_skills[key] = float(value)
    return user_skills


def is_file_bin(file_name):
    ''' Проверяет наличие файла user.bin, если нет создаёт его.
    Генерирует health, damage, armor.
    Формат файла бинарный.
    str --> True
    '''

    user_skills = {}

    if not os.path.exists(file_name):
        user_skills['name'] = file_name.split('.')[0]
        user_skills['health'] = random.randint(MIN_HEALTH, MAX_HEALTH)
        user_skills['damage'] = round(
            random.uniform(MIN_DAMAGE, MAX_DAMAGE), 1
        )
        user_skills['armor'] = round(random.uniform(MIN_ARMOR, MAX_ARMOR), 1)
        with open(file_name, 'wb') as file:
            pickle.dump(user_skills, file)
    return True


def init_bin(user):
    '''
    создаёт их. Загружает сущности из файла в словарь и возвращает его.
    '''

    file_name = user + '.bin'
    user_skills = {}

    if is_file_bin(file_name):
        with open(file_name, 'rb') as file:
            user_skills = pickle.load(file)

    return user_skills


def battle(attack, protection):
    '''dict --> int'''

    injury = attack['damage'] / protection['armor']
    return injury


def game(player_1, player_2, filetype='txt'):
    '''Игра.
    fileformat тип файла для хранения сущности: txt - текстовой,
    bin - бинарный
    string --> return 1'''

    if filetype == 'txt':
        skill_player_1 = init_txt(player_1)
        skill_player_2 = init_txt(player_2)
    elif filetype == 'bin':
        skill_player_1 = init_bin(player_1)
        skill_player_2 = init_bin(player_2)
    round_battle = 1

    while skill_player_1['health'] >= 0 and skill_player_2['health'] >= 0:
        print(f'Раунд {round_battle}')
        print(f'Атака {skill_player_1["name"]} на {skill_player_2["name"]}!')
        print(battle(skill_player_1, skill_player_2))
        skill_player_1['health'] -= battle(skill_player_1, skill_player_2)

        print(
            f'У игрока {skill_player_2["name"]} ',
            f'осталось {skill_player_2["health"]:.0f} единиц здоровья.'
            )
        print(f'Атака {skill_player_2["name"]} на {skill_player_1["name"]}!')

        skill_player_2['health'] -= battle(skill_player_2, skill_player_1)

        print(
            f'У игрока {skill_player_1["name"]} ',
            f'осталось {skill_player_1["health"]:.0f} единиц здоровья.'
            )

        round_battle += 1

    if skill_player_2['health'] <= 0 < skill_player_1['health']:
        print(f'Выиграл игрок {skill_player_1["name"]}!')
    elif skill_player_1['health'] <= 0 < skill_player_2['health']:
        print(f'Выиграл игрок {skill_player_2["name"]}!')
    else:
        print('Ничья')
    return 1


if __name__ == "__main__":
    game('player', 'enemy', 'txt')
    # game('player', 'enemy', 'bin')
