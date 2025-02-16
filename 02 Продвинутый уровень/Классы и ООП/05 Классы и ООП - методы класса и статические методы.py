"""
Классы в Python — это объекты, содержащие свойства и методы
Класс содержит:
Свойства(атрибуты(данные))
Методы(функции)

@classmethod and @staticmethod

"""

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x=0, y=0):
        print('Вызов __init__')
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y


v = Vector(1, 2)
print(Vector.validate(-3))
res = v.get_coord()
print(res)