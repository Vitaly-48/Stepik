"""
Решение задачи, часть в)
Алгоритм построения таблицы значений функции на интервале [a, b], количество значений n.

вычислить шаг h по формуле:
h = {b-a \over n-1}
h=
n−1
b−a
​

создать список x_list, содержащий все значения аргумента функции x,
список должен включать следующие значения:
a, a + h, a + 2 * h, a + 3 * h, ... , b
создать список y_list, содержащий все значения функции,
вычисленные от сформированных в списке  аргументов, список должен включать:
f(x_list[0]), f(x_list[1]), .. f(x_list[n-1])
вывести таблицу значений функции, в первом столбце которой будут располагаться элементы списка x_list,
во втором - соответствующие значения списка y_list.

Реализация
"""
# 1. Опишем функцию f(x):
import math

def f_x(x):
   try:
       y = 1 / (x+1) + x / (x-3)
   except:
       y = math.inf
   return y


# 2. Введем границы интервала построения a, b и количество значений на интервале n:
a = float(input("a = "))    # a = -1

b = float(input("b = "))    # b = 1

n = int(input("n = "))      # n = 10


# 3. Выполним проверку правильности ввода: количество значений должно быть больше 0, нижняя граница должна быть меньше верхней
if n < 0 or a >= b:

    print("Ошибочные входные данные")


# 4. Если все введено верно, вычислим шаг изменения аргумента функции:
else:
    h = (b - a) / (n - 1)


# 5. Сформируем списки аргументов и значений функции:
    x_list = [a + i * h for i in range(n)]

    f_list = [f_x(x) for x in x_list]


# 6. Выведем таблицу значений функции:
    for i in range(n):
        print ("%4.1f : %6.3f" % (x_list[i], f_list[i]))
# Результат выполнения программы:
    # при a = -1
    # при b = 1
    # при n = 10

# -1.0: inf
# -0.8: 4.706
# -0.6: 2.406
# -0.3: 1.600
# -0.1: 1.161
# 0.1: 0.862
# 0.3: 0.625
# 0.6: 0.416
# 0.8: 0.213
# 1.0: 0.000


# 7. Оформим вывод в виде привычной таблицы
    # (знак * при форматном выводе означает,
    # что строку "-" нужно повторить указанное количество раз) :

# вывод шапки таблицы
    print("-" * 17)
    print ("| %4s | %6s |" % ("x", "f(x)"))
    print("-" * 17)
    # вывод содержимого таблицы
    for i in range(n):
        print ("| %4.1f | %6.3f |" % (x_list[i], f_list[i]))
# вывод подчеркивания
    print("-" * 17)
# Результат выполнения программы:
# -----------------
# |    x |   f(x) |
# -----------------
# | -1.0 |    inf |
# | -0.8 |  4.706 |
# | -0.6 |  2.406 |
# | -0.3 |  1.600 |
# | -0.1 |  1.161 |
# |  0.1 |  0.862 |
# |  0.3 |  0.625 |
# |  0.6 |  0.416 |
# |  0.8 |  0.213 |
# |  1.0 |  0.000 |
# -----------------
