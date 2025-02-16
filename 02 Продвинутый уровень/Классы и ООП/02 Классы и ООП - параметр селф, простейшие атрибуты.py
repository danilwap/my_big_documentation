"""
Классы в Python — это объекты, содержащие свойства и методы
Класс содержит:
Свойства(атрибуты(данные))
Методы(функции)
"""

class Point:
    color = 'red'
    circke = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

        print(f"x = {self.x}, y = {self.y}")


    def get_coords(self):
        return f"x = {self.x}, y = {self.y}"


pt = Point()
pt2 = Point()
pt.set_coords(1, 2)
pt2.set_coords(10, 20)
print(pt.__dict__)
print(pt2.__dict__)
print(pt2.get_coords())

