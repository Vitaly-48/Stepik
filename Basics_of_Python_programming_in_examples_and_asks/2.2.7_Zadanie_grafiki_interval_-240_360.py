"""
Всё просто - берёте предыдущий урок(https://stepik.org/lesson/267709/step/9?unit=248684),
заменяете функции f_x(x) и f_y(x) на тутошние,
изменяете размер отрезка на [-240..360] и задаёте количество точек построения, н-р  6000.
Не забыть подключить библиотеку from math import *
radians(x) - перевод градусов в радианы.
Прорисуются графики - на них всё прекрасно видно.
"""

# import matplotlib.pyplot as plt
# from math import cos, sin, log, radians, exp
#
#
# def f_x(x):
#     f = exp(cos(radians(x))) + log(sin(0.8 * radians(x)) ** 2 + 1) * cos(radians(x))
#     return f
#
#
# def y_x(x):
#     k = -log((cos(radians(x)) + sin(radians(x))) ** 2 + 1.7) + 2
#     return k
#
#
# a = -360
# b = 360
# n = 100
# h = (b - a) / (n - 1)
#
# x_list = [a + h * i for i in range(n)]
#
# f_list = [f_x(x) for x in x_list]
#
# y_list = [y_x(x) for x in x_list]
#
# line1 = plt.plot(x_list, f_list, label='f_x')
# line2 = plt.plot(x_list, y_list, label='y_x')
#
# plt.setp(line1, color="yellow", linewidth=5)
#
# plt.setp(line2, color="red", linewidth=5)
#
# plt.gca().spines["left"].set_position("center")
# plt.gca().spines["bottom"].set_position("center")
# plt.gca().spines["top"].set_visible(False)
# plt.gca().spines["right"].set_visible(False)
# plt.legend()
# plt.show()


"""
import matplotlib.pyplot as plt
from math import cos, sin, radians, exp, log1p

def f_x(x):
    y = exp(cos(radians(x) + log1p((sin**2(radians(0.8 * x)) +1) * cos(x)
    return y

def y_x(x):
    y = -log1p((cos(x) + sin(x)) ** 2 + 1.7) + 2

    return y
"""

import matplotlib.pyplot as plt
import math


# 2. Опишем две функции:
def f_x(x):
    y = math.exp(math.cos(x)) + math.log((math.sin(0.8 * x) ** 2) + 1) * math.cos(x)
    return y


def y_x(x):
    y = -math.log((math.cos(x) + math.sin(x)) ** 2 + 1.7) + 2
    return y


# 3. Зададим интервал построения функции и количество точек построения. Вычислим шаг:
a = math.radians(-240)
b = math.radians(360)
n = 100
h = (b - a) / (n - 1)

# 4. Сформируем списки со значениями аргументов и значениями функций в них:
x_list = [a + h * i for i in range(n)]
f_list = [f_x(x) for x in x_list]
y_list = [y_x(x) for x in x_list]

# 5. Построим линии графиков функций, зададим подпись для вывода легенды:
line_f = plt.plot(x_list, f_list, label='f(x)')
line_y = plt.plot(x_list, y_list, label='y(x)')

# 6. Зададим стили линий:

plt.setp(line_f, color="blue", linewidth=2)
plt.setp(line_y, color="red", linewidth=2)

# 7. Выведем 2 оси, установим для них позицию zero:

plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

# 8. Выведем легенду и заголовок в область построения:

plt.legend()
plt.title("Графики функций")

# 9. Отобразим область построения:

plt.show()