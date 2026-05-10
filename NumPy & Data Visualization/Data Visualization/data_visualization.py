# data_visualization.py
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y, marker='o')
plt.title('Sample Line Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)
plt.show()
