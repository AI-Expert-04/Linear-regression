import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([1, 2, 3, 4])
y_data = np.array([10000, 20000, 30000, 40000])

plt.figure(0)
plt.plot(x_data, y_data, 'bo', label='y_data')
plt.legend()
plt.show()
