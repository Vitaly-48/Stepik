from matplotlib.patches import Wedge, Arc
import matplotlib.pyplot as plt

# вставить необходимые операторы
# задаём поле для рисунка
plt.xlim(0, 6)
plt.ylim(0 ,5)
ax = plt.gca()
# нарисовать сектор
figure_w = Wedge((3, 1), 2, 45, 135)  # сформировать сектор, параметры для цвета линии и заливки не указывать
ax.add_patch(figure_w)

# нарисовать дугу, для нее установить параметр  linewidth = 3
figure_a = Arc((3, 1), 6, 6, 0, 45, 135, lw=3)
ax.add_patch(figure_a)
ax = plt.gca()

plt.show()