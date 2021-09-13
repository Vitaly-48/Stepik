from math import ceil


a, b, v = float(input()), float(input()), int(input())

if (a <= 0) or (b <= 0) or (v <= 0):
    print("error")

else:
    print(ceil((a ** 2 * 5 * b) / (v * 1000)))