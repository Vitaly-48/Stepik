

def compute_resist(r_1, r_2):

   r = r_1 * r_2 / (r_1 + r_2)

   return r

res = compute_resist(12.0, 11.0)
print(res)



"""from math import sqrt


x_a, y_a, x_b, y_b, x_c, y_c = float(input()), float(input()), float(input()), float(input()), float(input()), float(input())


def compute_len(x_0, y_0, x_1, y_1):
    return sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)


a = compute_len(x_a, y_a, x_b, y_b)
b = compute_len(x_b, y_b, x_c, y_c)
c = compute_len(x_a, y_a, x_c, y_c)

if a + b <= c or b + c <= a or a + c <= b:
    print("error")

else:
    p = a + b + c
    s = sqrt(p / 2 * (p / 2 - a) * (p / 2 - b) * (p / 2 - c))
    r = sqrt(((p / 2 - a) * (p / 2 - b) * (p / 2 - c)) / (p / 2))
    R = (a * b * c) / (4 * s)
    Ma = sqrt(2 * (c ** 2 + b ** 2) - a ** 2) / 2
    Mb = sqrt(2 * (a ** 2 + c ** 2) - b ** 2) / 2
    Mc = sqrt(2 * (a ** 2 + b ** 2) - c ** 2) / 2
    print(round(r, 4), round(R, 4), round(Ma + Mb + Mc, 4))"""