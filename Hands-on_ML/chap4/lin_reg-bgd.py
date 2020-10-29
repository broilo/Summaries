import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

X = 2*np.random.rand(100, 1)
y = 4+3*X+np.random.randn(100, 1)

X_b = np.c_[np.ones((100, 1)), X]

theta_path_bgd = []


def plot_greadient_descent(theta, eta, theta_path=None):
    m = len(X_b)
    plt.plot(X, y, "b.")
    n_iterations = 1000
    for iteration in range(n_iterations):
        if iteration < 10:
            y_predict = X_new_b.dot(theta)
            style = "b-" if iteration > 0 else "r--"
            plt.plot(X_new, y_predict, style)
        gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)
        theta = theta - eta * gradients
        if theta_path is not None:
            theta_path.append(theta)
    plt.xlabel("$x_1$", fontsize=18)
    plt.axis([0, 2, 0, 15])
    plt.title(r"$\eta = {}$".format(eta), fontsize=16)


theta = np.random.randn(2, 1)  # random initialization

X_new = np.array(([0], [2]))
X_new_b = np.c_[np.ones((2, 1)), X_new]

plt.figure(figsize=(10, 4))
plt.subplot(131)
plot_greadient_descent(theta, eta=0.02)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.subplot(132)
plot_greadient_descent(theta, eta=0.1, theta_path=theta_path_bgd)
plt.subplot(133)
plot_greadient_descent(theta, eta=0.5)
plt.show()
