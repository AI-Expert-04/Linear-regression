import numpy as np
import matplotlib.pyplot as plt


def minumum_mean_square_error(y_predict, y_data):
    ret = 0
    for i in range(len(y_predict)):
        ret += (y_data[i] - y_predict[i]) ** 2
    ret /= len(y_predict)
    return ret


x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_data = np.array([8, 24, 28, 46, 44, 55, 79, 80, 99, 105])

mse_x = np.arange(-10, 30)
mse_y = []

for slope in mse_x:
    y_predict = slope * x_data
    error = minumum_mean_square_error(y_predict, y_data)
    mse_y.append(error)

mse_y = np.array(mse_y)

a = np.sum(x_data * y_data) / np.sum(x_data ** 2)
print(a)

plt.figure(0)
plt.plot(mse_x, mse_y, 'r-', label='minumum mean square error')
plt.axvline(x=a, color='b')
plt.axhline(y=minumum_mean_square_error(a * x_data, y_data), color='b')
plt.xlabel('slope')
plt.ylabel('mse')
plt.legend()
plt.show()
