# Задание
# Дан фрагмент программного кода:
import matplotlib.pyplot as plt

x_list = [1, 5, -3]
y_list = [-5, 6, 1 ]


#функция создания линии
line = plt.plot(x_list, y_list, "gv")
plt.setp(line, color="blue", linewidth=2)
plt.show()
# Сопоставьте функцию, которую нужно вставить в программу


#функция создания линии
line = plt.plot(x_list, y_list, "r--")
plt.setp(line, color="blue", linewidth=2)
plt.show()
# Сопоставьте функцию, которую нужно вставить в программу


#функция создания линии
line = plt.plot(x_list, x_list)
plt.setp(line, color="blue", linewidth=2)
plt.show()
# Сопоставьте функцию, которую нужно вставить в программу


#функция создания линии
line = plt.plot(x_list, y_list, "r+-")
plt.setp(line, color="blue", linewidth=2)
plt.show()
# Сопоставьте функцию, которую нужно вставить в программу


#функция создания линии
line = plt.plot(y_list, "gv")
plt.setp(line, color="blue", linewidth=13)
plt.show()
# Сопоставьте функцию, которую нужно вставить в программу