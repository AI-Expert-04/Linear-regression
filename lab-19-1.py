import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-20, 20)
y = x**2
dy = 2*x

plt.subplot(2, 1, 1)
plt.plot(x, y, 'b-', label='f(x)')
plt.axvline(x=0, color='r')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(x, dy, 'b-', label='f`(x)')
plt.axhline(y=0, color='r')
plt.axvline(x=0, color='r')
plt.legend()
plt.show()
