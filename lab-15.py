import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('input.txt', dtype=np.int, delimiter=',')
x_data = data[:, 0]
y_data = data[:, 1]

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
