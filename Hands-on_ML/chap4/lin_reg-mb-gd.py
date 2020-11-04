import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

X = 2*np.random.rand(100, 1)
y = 4+3*X+np.random.randn(100, 1)

X_b = np.c_[np.ones((100, 1)), X]

X_new = np.array(([0], [2]))
X_new_b = np.c_[np.ones((2, 1)), X_new]

t0, t1 = 200, 1000  # learning schedule hyperparameter


def learning_schedule(t):
    return t0 / (t + t1)


theta_path_mbgd = []


def plot_mbgd(theta, theta_path=None):
    m = len(X_b)
    n_epochs = 50
    n_interations = 50
    minibatch_size = 20
    t = 10
    plt.plot(X, y, "b.")
    plt.axis([0, 2, 0, 15])
    plt.xlabel("$x_1$", fontsize=18)
    plt.ylabel("$y$", rotation=0, fontsize=18)
    for epoch in range(n_interations):
        shuffled_indices = np.random.permutation(m)
        X_b_shuffled = X_b[shuffled_indices]
        y_shuffled = y[shuffled_indices]
        for i in range(0, m, minibatch_size):
            if epoch == 0 and i < 20:
                    y_predict = X_new_b.dot(theta)
                    style = "b-" if i > 0 else "r--"
                    plt.plot(X_new, y_predict, style)
            t += 1
            xi = X_b_shuffled[i:i+minibatch_size]
            yi = y_shuffled[i:i+minibatch_size]
            gradients = 2/minibatch_size * xi.T.dot(xi.dot(theta)-yi)
            eta = learning_schedule(t)
            theta = theta - eta * gradients
            theta_path_mbgd.append(theta)


np.random.seed(42)
theta = np.random.randn(2, 1)  # random initialization

plot_mbgd(theta, theta_path=theta_path_mbgd)
plt.show()
