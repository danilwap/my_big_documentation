"""
Что надо запомнить:
Преобразование типов — это преобразование объекта из одного типа данных в другой.
Неявное преобразование типов автоматически выполняется интерпретатором Python.
Python не допускает потери данных при неявном преобразовании типов.
Явное преобразование типов также называется приведением типов. Типы данных преобразуются пользователем с помощью встроенных функций.
В явном приведении типов может произойти потеря данных, поскольку мы принудительно приводим объект к определенному типу.
"""

"""
Пример как можно использовать исключения
try:
    file = open()
except Exception as e:
    print(e)
    
Ловля любого исключение и вывод в терминал



в try — код, который может вызвать исключения;
в except — код, который должен выполниться при возникновении исключения;
в finally — код, который должен выполниться в любом случае.

try:
    res = a + b
except TypeError:
    res = int(a) + int(b)
finally:
    print(f"a = {a}, b = {b}, res = {res}")
    
    
    
try:
    #  попробуем что-то сделать
except (ZeroDivisionError, ValueError) as e:
    #  обрабатываем исключения типа ZeroDivisionError или ValueError
except Exception as e:
    #  исключение не ZeroDivisionError и не ValueError
    #  поэтому обрабатываем исключение общего типа (унаследованное от Exception)
    #  сюда не сходят исключения типа GeneratorExit, KeyboardInterrupt, SystemExit
else:
    #  этот блок выполняется, если нет исключений
    #  если в этом блоке сделать return, он не будет вызван, пока не выполнился блок finally
finally:
    #  этот блок выполняется всегда, даже если нет исключений else будет проигнорирован
    #  если в этом блоке сделать return, то return в блоке
"""