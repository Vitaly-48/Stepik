# 1. Подключим модуль для построения графиков функций, дадим ему имя plt:
import matplotlib.pyplot as plt
from math import atan, pi

# 2. Опишем функцию:
def f_x(x):
   return (172 * (pi / 2 - atan((2000 - x) / 45)) / 45)

# 3. Зададим начало a и конец  b интервала построения функции, задав количество точек построения. Вычислим шаг:
a = 2000
b = 2013
n = 2
h = (b-a)/(n-1)

# 4. Сформируем списки со значениями аргументов и значениями функции в них:
x_list = [a + h * i for i in range(n)]
f_list = [f_x(x) for x in x_list]

# 5. Построим линию графика, установим для нее цвет и толщину:
line1 = plt.plot(x_list, f_list)
plt.setp(line1, color="blue", linewidth=13)

# 6. Сформируем списки со значениями аргументов
o_list = [2012, 2012, 2012]
p_list = [6, 6, 7]
u_list = [2000, 2012, 2012]
i_list = [7, 7, 7]

# 7. Построим линию графика 2, установим для нее цвет и толщину:
line2 = plt.plot(o_list, p_list, u_list, i_list)
plt.setp(line2, color="red", linewidth=1, marker="o")

# 8. Выведем 2 оси, установим для них позицию zero:
# plt.gca().spines["left"].set_position("center")
# plt.gca().spines["bottom"].set_position("center")
# plt.gca().spines["right"].set_position("zero")
# plt.gca().spines["top"].set_position("zero")
#plt.gca().spines["top"].set_visible(True)
#plt.gca().spines["bottom"].set_visible(True)
#plt.gca().spines["left"].set_visible(True)
#plt.gca().spines["right"].set_visible(True)

# 9. Отобразим область построения:
plt.show()


print('-------------------------------------------------------------------------------')


# Через консоль

# # Sample Output:
# # 2012 -  7.000 миллиард(ов)
# # 2167 - 11.000 миллиард(ов)
import math
from math import atan
from math import pi

def compute_population(t):
# вычислить численность населения для года t по формуле
    c = 172
    t1 = 2000
    tay = 45
    n = c / tay * (math.pi / 2 - math.atan((t1 - t) / tay))
    return n

#ввести строку с перечисленными через пробел годами
n = 2012
line = input()

# преобразовать строку в список из строковых значений годов
years_str_list = line.split()

# вычислить количество элементов в списке
n = len(years_str_list)

# сформировать список years_list на основе years_str_list,
#преобразовав строковые значения в целые
years_list = [int(a) for a in years_str_list]

# создать список population_list, каждый элемент которого вычисляется
# функцией compute_population от соответсвующего года из списка years_list
population_list = [compute_population(b) for b in years_list]

# в цикле для каждого года вывести численность населения, для вывода использовать
# формат "%5d - %6.3f миллиард(ов)"
for c in range(n):
    print("%5d - %6.3f миллиард(ов)" % (years_list[c], population_list[c]))

print('-----------------------------------------------------------------------------')


def compute_population(t):
   #вычислить численность населения для года t по формуле
    return (172 / 45) * ((pi / 2) - atan((2000 - t) / 45))

#ввести строку с перечисленными через пробел годами
line = input()

# преобразовать строку в список из строковых значений годов
years_str_list = line.split()

# вычислить количество элементов в списке
n = len(years_str_list)

# сформировать список years_list на основе years_str_list,
#преобразовав строковые значения в целые
#

# создать список population_list, каждый элемент которого вычисляется
# функцией compute_population от соответсвующего года из списка years_list
#

# в цикле для каждого года вывести численность населения, для вывода использовать
# формат "%5d - %6.3f миллиард(ов)"
for year in years_str_list:
    print(f'{int(year):5d} - {compute_population(int(year)):6.3f} миллиард(ов)')