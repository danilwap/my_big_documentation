# dict - словарь

"""
Получение данных
dictionary["марафон"]

Добавление и обновление
dictionary["туфля"] = "Какой-то текст"
dictionary["туфля"] = "Какой-то другой текст"

Удаление
del dictionary["Туфля"]
"""

"""
Методы словарей
.update({'бужал': "Какое-то понятие"}) - Добавляет в словарь другой словарь
.get('k') - возвращает значение ключа k, если отсутствует, то возвращается None
.get('k', n) - возвращает значение ключа k, если отсутствует, то возвращается n
.pop('k') - удаляет ключ и возвращает значение
.keys() - возвращает список ключей в словаре
.values() - возвращает список значений в словаре
.items() - возвращает список пар ключ - значение
"""

"""
Итерации через словарь
for key in dict:
    print(key)
    
for key, value in dictionary.items():
    print(key, value)
"""


dict_test = {1: 24, 2: 25}
result = dict_test.get(22)
print(result)