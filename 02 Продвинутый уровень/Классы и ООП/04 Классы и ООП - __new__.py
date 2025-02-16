"""
Классы в Python — это объекты, содержащие свойства и методы
Класс содержит:
Свойства(атрибуты(данные))
Методы(функции)


__new__(cls) - выполняется до создания класса

"""

class Vector:
    def __init__(self, x=0, y=0):
        print('Вызов __init__')
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y


v = Vector(1, 2)
res = v.get_coord()
print(res)