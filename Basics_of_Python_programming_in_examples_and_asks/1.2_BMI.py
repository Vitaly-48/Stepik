print("Ваше имя?")

name = input()

print("Привет, ", name, "!")

age, height, weight = int(input("Сколько Вам полных лет? ")), float(input("Ваш рост? ")), float(input("Ваш вес? "))

if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:
    print("Ошибочные входные данные")

else:
    description = ""
    bmi = round(weight / height ** 2, 2)

    if (age < 45 and bmi < 18.5) or (age >= 45 and bmi < 22):
        description = "недостаточной массой тела."
    elif (age < 45 and 18.5 < bmi < 24.99) or (age >= 45 and 22 < bmi < 26.99):
        description = "нормальной массой тела."
    elif (age < 45 and 25 < bmi < 29.99) or (age >= 45 and 27 < bmi < 31.99):
        description = "избыточной массой тела."
    elif (age < 45 and bmi >= 30) or (age >= 45 and bmi >= 32):
        description = "ожирением."

    print("bmi=", bmi, "Вы относитесь к группе людей с", description)
