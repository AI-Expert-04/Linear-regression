import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_data = np.array([58, 74, 78, 96, 94, 105, 129, 130, 149, 155])

A = np.sum(x_data)
B = np.sum(y_data)
C = np.sum(x_data ** 2)
D = np.sum(x_data * y_data)
k = len(x_data)

a = (k * D - A * B) / (k * C - A ** 2)
b = (B - a * A) / k

y = a * x_data + b

a2 = np.sum(x_data * y_data) / np.sum(x_data ** 2)

y2 = a2 * x_data

plt.figure(0)
plt.plot(x_data, y_data, 'ro', label='data')
plt.plot(x_data, y, 'b-', label='y=ax+b')
plt.plot(x_data, y2, 'g-', label='y=ax')
plt.legend()
plt.show()
