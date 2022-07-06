import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-20, 20)
y = x**2

px1 = np.array([-5])
py1 = px1**2


for px2 in np.arange(18, -5, -0.5):
    py2 = px2**2
    a = (py2 - py1) / (px2 - px1)
    b = py1 - a * px1
    y2 = a * x + b

    plt.figure(0)
    plt.plot(x, y, 'b-')
    plt.plot(px1, py1, 'ro')
    plt.plot(px2, py2, 'ro')
    plt.plot(x, y2, 'r-')
    plt.show()
