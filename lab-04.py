import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_data = np.array([8, 24, 28, 46, 44, 55, 79, 80, 99, 105])

plt.figure(0)
plt.plot(x_data, y_data, 'ro', label='y_data')
plt.legend()
plt.show()
