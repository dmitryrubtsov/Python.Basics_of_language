'''Задача - 1
Ранее мы с вами уже писали игру, используя словари в качестве структур данных
для нашего игрока и врага, давайте сделаем новую, но уже с ООП. Опишите базовый
класс Person, подумайте какие общие данные есть и у врага и у игрока Не
забудьте, что у них есть помимо общих атрибутов и общие методы.  Теперь
наследуясь от Person создайте 2 класса Player, Enemy.  У каждой сущности должны
быть атрибуты health, damage, armor У каждой сущности должно быть 2 метода,
один для подсчёта урона, с учётом брони противника, второй для атаки
противника. Функция подсчёта урона должна быть инкапсулирована Вам надо описать
игровой цикл так же через класс.  Создайте экземпляры классов, проведите бой.
Кто будет атаковать первым оставляю на ваше усмотрение.'''

import random

class Person:
    def __init__(self, name):
        self.name = name
        self.health = float(random.randint(40, 200))
        self.damage = round(random.uniform(0.5, 2.5), 1)
        self.armor = round(random.uniform(1.0, 2.5), 1)

    def info(self):
        print(
            f'{self.name} health: {self.health:.0f}',
            f'damage {self.damage}',
            f'armor {self.armor}'
              )

    def _atack(self, protection):
        injury = round(self.damage / protection, 1)
        return injury

    def _protection(self, damage):
        injury = round(damage / self.armor, 1)
        return injury

    def battle(self, enemy):
        self.health -= self._protection(enemy.damage)
        enemy.health -= self._atack(enemy.armor)


class Player(Person):
    pass


class Enemy(Person):
    pass


player1 = Player('player_1')
enemy1 = Enemy('enemy_1')

player1.info()
enemy1.info()

round_battle = 1

while player1.health > 0 and enemy1.health > 0:
    print(f'Раунд {round_battle}')
    player1.battle(enemy1)
    round_battle += 1

    player1.info()
    enemy1.info()

if player1.health <= 0 < enemy1.health:
    print(f'Выиграл игрок {enemy1.name}!')
elif enemy1.health <= 0 < player1.health:
    print(f'Выиграл игрок {player1.name}!')
else:
    print('Ничья')
