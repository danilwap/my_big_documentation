"""
Классы в Python — это объекты, содержащие свойства и методы
Класс содержит:
Свойства(атрибуты(данные))
Методы(функции)

Инициализатор и финализатор
__init__(self) - Инициализатор
__del__(self) - финализатор
"""

class Point:
    color = 'red'
    circke = 2

    def __init__(self, x=0, y=0):
        print('Вызов __init__')
        self.x = x
        self.y = y


    def __del__(self):
        print("Удаление экземпляра: " + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

        print(f"x = {self.x}, y = {self.y}")


    def get_coords(self):
        return f"x = {self.x}, y = {self.y}"

pt = Point()
print(pt.__dict__)
