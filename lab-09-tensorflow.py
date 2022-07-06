import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
tf1 = tf.compat.v1
tf1.set_random_seed(777)

x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_data = np.array([8, 24, 28, 46, 44, 55, 79, 80, 99, 105])

g = tf1.Graph()
with g.as_default() as graph:
    # W = tf1.Variable(tf1.random_normal([1]))
    W = tf1.placeholder(tf.float32)
    b = tf1.Variable(tf1.zeros([1]))

    hypothesis = W * x_data + b

    cost = tf1.reduce_mean(tf1.square(y_data - hypothesis))

    x = np.arange(-10, 30)
    y = []

    with tf1.Session(graph=g) as sess:
        sess.run(tf1.global_variables_initializer())
        for xx in x:
            error = sess.run(cost, feed_dict={W: xx})
            y.append(error)
        y = np.array(y)

    plt.figure(0)
    plt.plot(x, y, 'b-')
    plt.show()

