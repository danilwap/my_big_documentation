# list - список

"""
numbers = [1, 2]
numbers[1] = 3  #в ковычках index места, должно быть меньше длины списка
Обновлённый список: [1, 3]
"""

"""
Создание списка
numbers = [1, 2, 3, 4, 5, 6]

word = list('tproger')
# ['t', 'p', 'r', 'o', 'g', 'e', 'r']

Генератор списка
numbers = [i for i in range(1, 6)]
# [1, 2, 3, 4, 5]
"""


"""
Срезы (slice) списка
numbers = [1, 5, 9, 6]
print(numbers[0:2])
# [1, 5]

numbers = [1, 5, 9, 6]
print(numbers[:3])
# [1, 5, 9]

numbers = [1, 5, 9, 6]
print(numbers[1:])
# [5, 9, 6]
"""

"""
Операции над списками
x in list - True, если элемент x есть в списке
x not in list - True, если элемент x есть в списке
list1 + list2 - Объединение двух списков
list1 * n - копирует список n раз
len(list1) - количество элементов в списке
min(list1) - наименьший элемент если число, если буква, то начальная буква алфавита
max(list1) - наибольший элемент
sum(list1) - сумма чисел списка
for i in list() - Перебирает числа слева направо
"""

"""
Методы(функции) списков python
.index(n) - индекс первого найденный n 
.count(n) - количество n в списке
.append(n) - добавляется n в конец списка
.sort() - сортирует от большего к меньшему
.sort(reverse = true) - сортирует от меньшего к большему
.insert(n, m) - вставляет элемент m, на позицию n(индекс)
.remove(n) - удаляет первый попавшийся n в списке
.extend([1,2]) - добавляет список в конец списка
.pop(m) - извлекает элемент с индексом m
str = ', '.join(list) преобразует список в строку
"""
