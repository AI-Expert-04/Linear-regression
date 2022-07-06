import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([1, 2, 3, 4])
y_data = np.array([10000, 20000, 30000, 40000])
fx_data = 10000 * x_data  # y = 10000 * x

plt.figure(0)
plt.plot(x_data, y_data, 'ro', label='y_data')
plt.plot(x_data, fx_data, 'b-', label='fx_data')
plt.legend()
plt.show()
