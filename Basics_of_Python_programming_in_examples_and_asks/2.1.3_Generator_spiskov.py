# Кроме явного создания списков, как например:
x_list = [3, 6, 23]
print("Явный список:", x_list)
# Список:  [3, 6, 23]


# их можно создавать с помощью генератора.
"""
Генератор списков - способ построить новый список, применяя выражение к каждому элементу диапазона или другого списка.
Для создания списка, элементы которого формируются в зависимости от значения переменной-диапазона i, используется следующий оператор:
список = [формула_от_i for i in range(описание диапазона)]
Примеры создания подобных списков:
"""
x_list = [2 * i + 1 for i in range(5)]
print("Сгенерированный список:", x_list)
# Сгенерированный список:  [1, 3, 5, 7, 9]

x_list = [i for i in range(5,10,2)]
print("Сгенерированный список:", x_list)
# Сгенерированный список:  [5, 7, 9]

x_list = [2*i for i in range(3,-3,-1)]
print("Сгенерированный список:", x_list)
# Сгенерированный список:  [6, 4, 2, 0, -2, -4]


"""
Генерация списков осуществляется не только с использованием диапазонов, но и других списков:
новый_список = [формула_от_x for x in список]
Примеры генерации списков на основе уже существующих:
"""
x_list = [5, 8, -5]
y_list = [x ** 2 for x in x_list]
print("Сгенерированный список на основе уже существующего:", y_list)
# Сгенерированный список на основе уже существующего:  [25, 64, 25]

x_list = [3, 2, 7]
y_list = [x % 2 for x in x_list]
print("Сгенерированный список на основе уже существующего:", y_list)
# Сгенерированный список на основе уже существующего:  [1, 0, 1]


"""
Ввод списка на основе строки

Алгоритм формирования списка:
пользователь вводит элементы списка в одной строке через пробел, ввод заносится в строковую переменную;
полученную строку необходимо преобразовать в список с помощью метода split(), при этом в список будет занесены введенные числа в виде строк;
преобразовать элементы списка из строковых в вещественные.
Пример.

Введем с клавиатуры  вещественные числа и занесем их в список.
"""
# вводим строку с числами: 3.5 6 7.34 -6.213 0
line = input()

# преобразуем строку в список, элементы которого - строки
str_list = line.split()

print("Список из строк :", str_list)
# Список из строк : ['3.5', '6', '7.34', '-6.213', '0']

# создаем новый список на основе уже сформированного,
# переводя каждый элемент в вещественное число
x_list = [float(x) for x in str_list]

print("Новый список на основе уже сформированногописок из вещественных чисел", x_list)
# Новый список на основе уже сформированногописок из вещественных чисел [3.5, 6.0, 7.34, -6.213, 0.0]
