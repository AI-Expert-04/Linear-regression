import numpy as np

error = np.array([-0.58181818, 4.7030303, -2.01212121, 5.27272727, -7.44242424,
                  -7.15757576, 6.12727273, -3.58787879, 4.6969697, -0.01818182])

ret = 0
for e in error:
    ret += e ** 2
ret /= len(error)

print(ret)
