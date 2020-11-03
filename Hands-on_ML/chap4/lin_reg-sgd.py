"""
There's an error in this code, because the figure
plotted at the end is different from the one shown
in the book (Fig. 4-10). Moreover, the result is
different from that obtained using the Batch Gradient
Descent algorithm.
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

X = 2*np.random.rand(100, 1)
y = 4+3*X+np.random.randn(100, 1)

X_b = np.c_[np.ones((100, 1)), X]

X_new = np.array(([0], [2]))
X_new_b = np.c_[np.ones((2, 1)), X_new]

t0, t1 = 5, 50  # learning schedule hyperparameter


def learning_schedule(t):
    return t0 / (t + t1)


theta_path_sgd = []


def plot_sgd(theta, theta_path=None):
    m = len(X_b)
    n_epochs = 50
    plt.plot(X, y, "b.")
    plt.axis([0, 2, 0, 15])
    plt.xlabel("$x_1$", fontsize=18)
    plt.ylabel("$y$", rotation=0, fontsize=18)
    for epoch in range(n_epochs):
        for i in range(m):
            if epoch == 0 and i < 20:
                y_predict = X_new_b.dot(theta)
                style = "b-" if i > 0 else "r--"
                plt.plot(X_new, y_predict, style)
            random_index = np.random.randint(m)
            xi = X_b[random_index:random_index+1]
            yi = y[random_index:random_index+1]
            gradients = 2 * xi.T.dot(xi.dot(theta) - yi)
            eta = learning_schedule(epoch * m + i)
            theta = theta - eta * gradients
            theta_path_sgd.append(theta)


theta = np.random.randn(2, 1)  # random initialization

plot_sgd(theta)
plt.show()
