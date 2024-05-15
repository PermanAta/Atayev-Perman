import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

# Заданные точки
points = np.array([
    [2, 5],
    [3, 2],
    [5, -7],
    [7, 7],
    [9, 7]
])

# Выполнение триангуляции Делоне
tri = Delaunay(points)

# Визуализация триангуляции
plt.triplot(points[:, 0], points[:, 1], tri.simplices)
plt.plot(points[:, 0], points[:, 1], 'o')

# Подписи точек
for idx, (x, y) in enumerate(points):
    plt.text(x, y, f'A{idx+1} ({x}, {y})', fontsize=12, ha='right')

plt.xlabel('X координата')
plt.ylabel('Y координата')
plt.title('Триангуляция Делоне')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
