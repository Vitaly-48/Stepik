# put your python code here
year = int(input())

if year < 1582:
    print("error")

else:
    if (year % 4 == 0) and not (year % 100 == 0 and year % 400 != 0):
        print("366")
    else:
        print("365")