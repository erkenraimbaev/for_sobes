from abc import ABC, abstractmethod


class Bird(ABC):
    """
    Absctract class
    """

    def __init__(self, count):
        self.count = count

    @abstractmethod
    def tell_about_me(self):
        print('   ')


class Human:
    """
    People class
    """

    def __init__(self, name, defend_level):
        self.name = name
        self.defend_level = defend_level


class Nechto(Human, Bird):
    """
    What is it
    """

    def __init__(self, name, danger_level, defend_level):
        super().__init__(name, defend_level)
        self.danger_level = danger_level

    def __str__(self):
        return f'{self.name} FFF'

    def __add__(self, other):
        return self.danger_level + other.danger_level

    # def __gt__(self, other):
    #     return self.defend_level > other.defend_level

    def __ge__(self, other):
        return self.defend_level >= other.defend_level

    def tell_about_me(self):
        return f'I am monster'


nechto = Nechto('A', 5, 11)
nechto.other = 5
nechto1 = Nechto('B', 7, 11)
print(nechto.__dict__)
print(nechto.tell_about_me())
# print(nechto > nechto1)
print(nechto == nechto1)


class Pterodactil:
    __slots__ = ('rost', 'ves')
    PTERO_VALUE = 1000


ptero = Pterodactil()
ptero.ves = 'FFF'
print(ptero.__dict__)
