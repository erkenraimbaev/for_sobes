import datetime
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Class for making animals
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def to_be(self):
        pass

    @staticmethod
    def get_time():
        date = datetime.datetime.now()
        return f'Today is {date}'


class Dog(Animal):
    """
    It is dog
    """

    def __init__(self, weight, age, name):
        super().__init__(name)
        self.__weight = weight
        self._age = age

    def to_be(self):
        print(f'He lives')


# animal = Animal()
dog1 = Dog('Dog', 10, 5)
# print(dog1.__weight)
dog1._age = 6
print(dog1.__dir__())
print(dog1.__dict__)


class Wolf(Animal):
    """
    Wolf it is
    """

    def to_be(self):
        print(f'I am wolf')


wolf1 = Wolf('Akela')


class Coyot(Dog, Wolf):
    """
    It is monster
    """
    numbers_of_coyots = 0

    @classmethod
    def _how_many_eat(cls, number: int):
        print(f'I am a son of wolf and dog!')
        cls.numbers_of_coyots += number

    @property
    def get_info(self):
        return f'{self.name}'

    @get_info.setter
    def get_info(self, name):
        if len(name) < 5:
            self.name = name
        else:
            print('It is not good!')

    @get_info.deleter
    def get_info(self):
        print('Delete')
        self.name = None


coyot1 = Coyot(12, 10, 'Monster')
print(coyot1.to_be())
print(Coyot._how_many_eat(10))
print(coyot1.numbers_of_coyots)
print(coyot1.get_time())
print(coyot1._Dog__weight)
# print(coyot1.get_info)
coyot1._age = 15
print(coyot1.get_info)
del coyot1.get_info
print(coyot1.__dict__)
print(Coyot.mro())
