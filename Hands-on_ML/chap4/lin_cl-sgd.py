import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor

np.random.seed(42)

X = 2*np.random.rand(100, 1)
y = 4+3*X+np.random.randn(100, 1)

sgd_reg = SGDRegressor(max_iter=1000, tol=1e-3,
                       penalty=None, eta0=0.1, random_state=42)
sgd_reg.fit(X, y.ravel())
sgd_reg.intercept_, sgd_reg.coef_

X_new = np.array([[0], [2]])

y_predict = sgd_reg.predict(X_new)

plt.plot(X_new, y_predict, "r-")
plt.plot(X, y, "b.")
plt.axis([0, 2, 0, 15])
plt.show()
