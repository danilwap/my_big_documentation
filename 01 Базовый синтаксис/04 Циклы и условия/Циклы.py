"""
break — прерывает цикл и выходит из него;
continue — прерывает текущую итерацию и переходит к следующей.
else - выполняется, когда выход из цикла был после окончания, а не break

for i in range(10):
    print(i)
else:
    print('end')
else вступает в работу после окончания перебора


n = 6
while n >= 0:
    print(n)
    n -= 1

iter = 6
while iter > 0:
    iter -= 1
    if iter == 3:
        continue
    print(iter)
print('Конец цикла')

continue - запускает итерацию заново

range(stop);
range(start, stop);
range(start, stop, step).
range(start, stop, -step). - последовательность в обратную сторону

enumerate(text) - создаёт последовательность с индексами

Генераторы списков
правило: [результирующее выражение | цикл | опциональное условие]

[i for i in "banaba"]
[x for x in range(30) if x % 2 == 0] - генератор с условием
    """
text = 'создаёт последовательность с индексами'
for i in enumerate(text):
    print(i)
