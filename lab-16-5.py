import numpy as np

data = np.loadtxt('data5.txt', dtype=np.str)
x_data = data[:, 0]
y_data = data[:, 1]

y_data = np.array(y_data, dtype=np.int)

print(type(y_data[0]))

print(x_data)
print(y_data)
