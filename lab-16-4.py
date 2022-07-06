import numpy as np

data = np.loadtxt('data4.txt', dtype=np.str, delimiter=',')
x_data = data[0, :]
y_data = data[1, :]

print(x_data)
print(y_data)
