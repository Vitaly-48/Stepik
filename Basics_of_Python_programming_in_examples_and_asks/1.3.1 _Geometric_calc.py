from math import asin, cos, sqrt, pi

x = float(input())
y = float(input())

# вычислить выражение, результат занести в переменную z

z = ((asin(cos(x + (sqrt(3) / 2) * pi))) + (1.2 * sqrt(2 - (cos(y) ** 2)))) / (x ** 2 + y ** 2 + 1)
print(round(z, 5))
