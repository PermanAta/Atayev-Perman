import matplotlib.pyplot as plt

# Определение координат вершин полигона
polygon = [
    (0, 0),    # A1
    (3, -1),   # A2
    (7, 1),    # A3
    (10, -2),  # A4
    (10, -4),  # A5
    (12, -7)   # A6
]

# Определение координат секущих узлов
A4_1 = (10, -10/3)
A6_1 = (10, -35/6)

# Разбиение полигона на выпуклые части
part1 = [polygon[0], A4_1, A6_1, polygon[0]]  # A1A4^1A6^1A1
part2 = [polygon[1], polygon[2], polygon[3], A4_1, polygon[1]]  # A2A3A4A4^1A2
part3 = [polygon[4], polygon[5], A6_1, polygon[4]]  # A5A6A6^1A5

# Функция для отрисовки полигона
def draw_polygon(vertices, color='blue'):
    vertices.append(vertices[0])  # Замкнуть полигон
    xs, ys = zip(*vertices)
    plt.plot(xs, ys, color=color)

# Отрисовка исходного полигона
draw_polygon(polygon, 'blue')

# Отрисовка разбиений
draw_polygon(part1, 'red')
draw_polygon(part2, 'green')
draw_polygon(part3, 'purple')

# Настройка графика
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Разбиение полигона на выпуклые части')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')

# Показ графика
plt.show()
