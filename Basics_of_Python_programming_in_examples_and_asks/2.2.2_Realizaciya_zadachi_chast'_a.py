# Реализация задачи, часть а)
# 1. Подключим модуль для построения графиков функций, дадим ему имя plt:

import matplotlib.pyplot as plt
# 2. Опишем функцию:

def f_x(x):

   y = x ** 3 - 6 * x ** 2 +  x + 5

   return y
# 3. Зададим начало a и конец  b интервала построения функции, задав количество точек построения. Вычислим шаг:

a = -2

b = 6

n =100

h = (b-a)/(n-1)
# 4. Сформируем списки со значениями аргументов и значениями функции в них:

x_list = [a + h * i for i in range(n)]

f_list = [f_x(x) for x in x_list]
# 5. Построим линию графика, установим для нее цвет и толщину:

line = plt.plot(x_list, f_list)

plt.setp(line, color="blue", linewidth=2)
# 6. Выведем 2 оси, установим для них позицию zero:

plt.gca().spines["left"].set_position("zero")

plt.gca().spines["bottom"].set_position("zero")

plt.gca().spines["top"].set_visible(False)

plt.gca().spines["right"].set_visible(False)
# 7. Отобразим область построения:

plt.show()
# В результате будет построен следующий график: