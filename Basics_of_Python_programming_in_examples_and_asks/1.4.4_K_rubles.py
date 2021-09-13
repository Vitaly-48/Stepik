n = int(input())

if 0 < n <= 99:
    if (n % 10 in [0, 5, 6, 7, 8, 9]) or (n in range(11, 15)):
        print(n, "рублей")

    elif n % 10 in [2, 3, 4]:
        print(n, "рубля")

    elif n % 10 == 1:
        print(n, "рубль")

else:
    print("ошибка")