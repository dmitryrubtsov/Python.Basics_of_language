#!/usr/bin/python3
''' == Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных
цифр, расположенных по возрастанию. Все цифры в карточке уникальный.
Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

'''

from os import name, system
from random import choice, randint, sample


class GameCard:
    '''Класс создания игровой карточки'''
    def __init__(self, user_name):
        self.user_name = user_name
        self._card = self._generate_card()

    def print_card(self):
        '''Функция вывода игровой карточки на экран'''
        offset = 2
        print(f'Игрок: {self.user_name}'.center(26, '-'))
        for i, num in enumerate(self._card):
            num = str(num)
            if (i + 1) % 9 != 0:
                print(num.rjust(offset), end=' ')
            else:
                print(num.rjust(offset))
        print(''.center(26, '-'))

    def _generate_card(self):
        '''Функция генерирует игровую карточку'''
        gen = [num for num in range(1, 91)]
        card = []

        for _ in range(3):
            line = sorted(sample(gen, 5))
            for i in line:
                gen.remove(i)
            for _ in range(4):
                line.insert(randint(0, 9), ' ')
            card.extend(line)
        return card

    def player_move(self, cask):
        '''Ход в игре. Вычёркивание цифры cask в карточке.'''
        if cask in self._card:
            self._card[self._card.index(cask)] = '\u2718'

    def is_win(self):
        flag = True
        for num in self._card:
            if isinstance(num, int):
                flag = False
        return flag


class UserCard(GameCard):
    '''Класс создания игровой карточки для игрока'''
    def player_move(self, cask):
        answer = input('Зачеркнуть цифру? (y/n) ').lower()
        if answer == 'y':
            if cask in self._card:
                super().player_move(cask)
                flag = True
            else:
                flag = False
                print(f'Номера {cask} нет на карточке. Вы проиграли.')
        else:
            if cask in self._card:
                flag = False
                print(f'Номер {cask} есть на карточке. Вы проиграли.')
            else:
                flag = True
        return flag


class CompCard(GameCard):
    '''Класс создания игровой карточки для компьютера'''
    pass


class GameLotto:
    '''Класс игры'''
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self._bag = [num for num in range(1, 91)]

    def start(self):
        'Начало игры'
        while True:
            self._clear()
            self.player.print_card()
            self.computer.print_card()
            if self.player.is_win() and self.computer.is_win():
                print('Ничья.')
                break
            elif self.player.is_win():
                print(f'Выиграл игрок {self.player.user_name}')
                break
            elif self.computer.is_win():
                print(f'Выиграл игрок {self.computer.user_name}')
                break
            else:
                new_cask = self._number_taken_from_bag()
                print(
                    f'Новый бочонок: {new_cask:2d} ',
                    f'(осталось {len(self._bag):2d})'
                )
                user_flag = self.player.player_move(new_cask)
                self.computer.player_move(new_cask)
                if user_flag:
                    continue
                else:
                    break

    def _number_taken_from_bag(self):
        try:
            cask = choice(self._bag)
            self._bag.remove(cask)
        except IndexError:
            print('Ошибка! в мешке не осталось бочонков.')
            exit()
        return cask

    def _clear(self):
        '''Функция очистки экрана.'''
        # for mac and linux
        if name == 'posix':
            _ = system('clear')

        # for windows
        elif name == 'nt':
            _ = system('cls')


USER_CARD = UserCard('user')
COMP_CARD = CompCard('comp')
GAME = GameLotto(USER_CARD, COMP_CARD)
GAME.start()
