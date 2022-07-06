import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_data = np.array([8, 24, 28, 46, 44, 55, 79, 80, 99, 105])

p = np.polyfit(x_data, y_data, 1)
linear_regression_y = np.polyval(p, x_data)

print('y = ' + str(p[0]) + 'x + (' + str(p[1]) + ')')

plt.figure(0)
plt.plot(x_data, y_data, 'ro', label='y_data')
plt.plot(x_data, linear_regression_y, 'b-', linewidth=3, label='linear regression')
plt.legend()
plt.show()
