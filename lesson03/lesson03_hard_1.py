''' Задание - 1
Давайте опишем пару сущностей player и enemy через словарь, который будет иметь
ключи и значения:
name - строка полученная от пользователя,
health - 100,
damage - 50.
Поэксперементируйте с значениями урона и жизней по желанию.
Теперь надо создать функцию attack(person1, person2), аргументы можете указать
свои, функция в качестве аргумента будет принимать атакующего и атакуемого,
функция должна получить параметр damage атакующего и отнять это количество
health от атакуемого.
Функция должна сама работать с словарями и изменять их значения.'''


PLAYER = {'name': 'player', 'health': 40, 'damage': 1}
ENEMY = {'name': 'enemy', 'health': 50, 'damage': 2}


def battle(attack, protection):
    '''dict --> dict'''

    protection['health'] -= attack['damage']
    return attack, protection


round = 1
while PLAYER['health'] > 0 and ENEMY['health'] > 0:
    print(f'Раунд {round}')
    print(f'Атака {PLAYER["name"]} на {ENEMY["name"]}!')
    battle(PLAYER, ENEMY)
    print(
        f'У игрока {ENEMY["name"]} осталось {ENEMY["health"]} единиц здоровья.'
        )
    print(f'Атака {ENEMY["name"]} на {PLAYER["name"]}!')
    battle(ENEMY, PLAYER)
    print(
        f'У игрока {PLAYER["name"]} осталось {PLAYER["health"]} единиц \
здоровья.'
        )

    round += 1

if PLAYER['health'] > 0 and ENEMY['health'] <= 0:
    print(f'Выиграл игрок {PLAYER["name"]}!')
elif ENEMY['health'] > 0 and PLAYER['health'] <= 0:
    print(f'Выиграл игрок {ENEMY["name"]}!')
else:
    print('Ничья')
