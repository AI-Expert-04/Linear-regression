import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-20, 20)
y = x**2

px = np.array([-5, 15])
py = px**2

print(px)
print(py)

a = (py[1] - py[0]) / (px[1] - px[0])
b = py[0] - a * px[0]

y2 = a * x + b

print(a)

plt.figure(0)
plt.plot(x, y, 'b-', label='f1')
plt.plot(px, py, 'ro')
plt.plot(x, y2, 'r-', label='f2')
plt.legend()
plt.show()
