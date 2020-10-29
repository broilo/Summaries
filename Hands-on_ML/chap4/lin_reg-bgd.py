import numpy as np
import matplotlib as plt

np.random.seed(42)

X = 2*np.random.rand(100, 1)
y = 4+3*X+np.random.randn(100, 1)

X_b = np.c_[np.ones((100, 1)), X]

theta_path_bgd = []


def plot_greadient_descent(theta, eta, theta_path=None):
    m = len(X_b)
    plt.plot(X,y)

plt.plot(X, y, "b.")
plt.axis([0, 2, 0, 15])
plt.show()

