import numpy as np

data = [[str(i) + str(j) for j in range(10)] for i in range(10)]
# Error
# a = data[1:7, 2:7]

data = np.array(data)
print(data)

a = data[1:7, 2:7]
print(a)
