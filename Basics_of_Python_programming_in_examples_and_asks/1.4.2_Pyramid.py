# put your python code here
from math import sqrt

a, h = float(input()), float(input())

if a <= 0 or h <= 0:
    print("error")

else:
    V = (a ** 2 * h) / (4 * sqrt(3))
    S = ((a ** 2 * sqrt(3)) / 4) + ((3 * a) / 2) * sqrt(h ** 2 + (a ** 2) / 12)

    print(round(V, 3), round(S, 3))