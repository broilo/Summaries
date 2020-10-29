import numpy as np

np.random.seed(42)

X = 2*np.random.rand(100, 1)
y = 4+3*X+np.random.randn(100, 1)

X_b = np.c_[np.ones((100, 1)), X]

eta = 0.1  # learning rate
n_iterations = 1000
m = 100

theta = np.random.randn(2, 1)  # random initialization

for iteration in range(n_iterations):
    gradients = 2/m * X_b.T.dot(X_b.dot(theta)-y)
    theta = theta - eta * gradients

theta

X_new = np.array(([0], [2]))
X_new_b = np.c_[np.ones((2, 1)), X_new]

X_new_b.dot(theta)