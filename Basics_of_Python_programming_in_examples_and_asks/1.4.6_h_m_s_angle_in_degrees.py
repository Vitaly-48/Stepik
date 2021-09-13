h, m, s = int(input()), int(input()), int(input())

if (0 <= h <= 11) and (0 <= m <= 59) and (0 <= s <= 59):
    print(round(h * 30 + m * 0.5 + s * (0.5 / 60), 2))

else:
    print("error")