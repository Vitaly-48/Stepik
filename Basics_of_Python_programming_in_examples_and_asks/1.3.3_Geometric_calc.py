from math import acos, degrees, hypot, sqrt

area = lambda a,b,c,hp: sqrt(hp * (hp-a) * (hp-b) * (hp-c))
angl = lambda a,b,c: degrees(acos((a*a + b*b - c*c) / (2*a*b)))

ax, ay, bx = float(input('x_a = ')), float(input('y_a = ')), float(input('x_b = '))
by, cx, cy = float(input('y_b = ')), float(input('x_c = ')), float(input('y_c = '))
a, b, c    = hypot(cx-bx, cy-by),    hypot(cx-ax, cy-ay),    hypot(bx-ax, by-ay)
p          = a+b+c

if (p-a <= a or p-b <= b or p-c <= c): print('Треугольник не существует')
else:
    print("Стороны: ", round(a,3), round(b,3), round(c,3))
    print("Площадь: ", round(area(a,b,c,p/2),3))
    print("Периметр: ", round(p,3))
    print("Углы: ", round(angl(c,b,a),3), round(angl(c,a,b),3), round(angl(a,b,c),3))
