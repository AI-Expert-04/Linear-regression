import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_data = np.array([8, 24, 28, 46, 44, 55, 79, 80, 99, 105])
# y_data = np.array([18, 34, 38, 56, 54, 65, 89, 90, 109, 115])

A = np.sum(x_data)
B = np.sum(y_data)
C = np.sum(x_data ** 2)
D = np.sum(x_data * y_data)
k = len(x_data)

a = (k * D - A * B) / (k * C - A ** 2)
b = (B - a * A) / k

y = a * x_data + b

plt.figure(0)
plt.plot(x_data, y_data, 'ro', label='data')
plt.plot(x_data, y, 'b-', label='y=ax+b')
plt.legend()
plt.show()
