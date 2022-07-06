import numpy as np

data = np.loadtxt('data3.txt', dtype=np.str)
x_data = data[0, :]
y_data = data[1, :]

print(x_data)
print(y_data)
