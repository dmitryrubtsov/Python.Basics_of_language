'''Задача - 2
Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо
в классе фабрика исходя из типа игрушки отдавать конкретный объект класса,
который наследуется от базового - Игрушка '''



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

class SoftToys:
    def production(self):
        print(f'Создана мягкая игрушка')

class Dolls:
    def production(self):
        print(f'Создана кукла')

class Factory(Toys):
    def __init__(self, name, model, color):
        super().__init__(name, model, color)
        self.name_factory = 'some factory'
        self.number_factory = '123123'
        if self.model == 'dolls':
            Dolls().production()
        if self.model == 'soft toys':
            SoftToys().production()

toy1 = Factory('toy', 'dolls', 'green')
toy2 = Factory('toy', 'soft toys', 'blue')
