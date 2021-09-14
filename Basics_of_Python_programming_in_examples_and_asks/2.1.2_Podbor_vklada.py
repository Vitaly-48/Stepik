from math import *

# deposit - сумма вклада,
# interest_rate -процентная ставка,
# # amount_months - количество месяцев

def compute_income(deposit, interest_rate, amount_months):
    # вычислить прибыль
    z = deposit * (1 + interest_rate / (12 * 100)) ** amount_months
    return z

print("Процент вклада k = ")
k = float(input())      # занести процент вклада = 8.0 %.

print("Количество месяцев n = ")
n = int(input())      # занести количество месяцев = 12 месяцев.

print("Прибыль s = ")
s = float(input())   # занести прибыль = 703.0 рубля.

for x in range(1000, 30000):
    # вычислить прибыль для вклада x с помощью функции compute_income(x, ..., ...)
    income = compute_income(x, k, n) - x
    if round(income) == s:
        # вывести значение вклада x
        print("%d" % x)
