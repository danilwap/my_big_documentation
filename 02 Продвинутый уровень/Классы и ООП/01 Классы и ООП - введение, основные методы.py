"""
Видео по теме
https://www.youtube.com/playlist?list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E

Классы в Python — это объекты, содержащие свойства и методы
Класс содержит:
Свойства(атрибуты)
Методы


Работа с классами
hasattr(Point, 'name_attr') - проверяет наличие атрибута
del Point.name_attr - удаляет атрибут
getattr(Point, 'name_attr') - показывает значение атрибута, если не существует, то возвращает ошибку
getattr(Point, 'name_attr', name_brake) - показывает значение атрибута, если не существует, то возвращает 'name_brake'
delattr(Point, 'name_attr') - удаляет атрибут, если нет, то ошибка
setatty(obj, name, value) - задаёт значение атрибута (если атрибут не существует, то он создаётся)

__doc__ - содержит строку с описанием класса
__dict__ - содержит набор атрибутов экземпляра класса

"""


class Point:
    'Тест описания класса'
    color = 'red'
    circle = 2


print(Point.__doc__)
