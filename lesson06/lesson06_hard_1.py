'''Задача - 1
Вам необходимо создать завод по производству мягких игрушек для детей. Вам надо
продумать структуру классов, чтобы у вас был класс, который создаёт игрушки на
основании: Названия, Цвета, Типа (животное, персонаж мультфильма) Опишите
процедуры создания игрушки в трёх методах: -- Закупка сырья, пошив, окраска Не
усложняйте пусть методы просто выводят текст о том, что делают. В итоге ваш
класс по производству игрушек должен вернуть объект нового класса Игрушка.'''



class Toys:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
        self._purchase_materials()
        self._sewing()
        self._painting()

    def _purchase_materials(self):
        print(f'Закупка сырья для {self.name}')

    def _sewing(self):
        print(f'Пошив {self.name}')

    def _painting(self):
        print(f'Окраска {self.name} в {self.color}')

class Factory(Toys):
    def __init__(self, name, model, color):
        super().__init__(name, model, color)
        self.name_factory = 'some factory'
        self.number_factory = '123123'

toy1 = Factory('toy', 'animal', 'green')
