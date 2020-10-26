import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(42)

X = 2*np.random.rand(100, 1)
y = 4+3*X+np.random.randn(100, 1)

lin_cl = LinearRegression()
lin_cl.fit(X, y)
lin_cl.intercept_, lin_cl.coef_

X_new = np.array([[0], [2]])

y_predict = lin_cl.predict(X_new)

plt.plot(X_new, y_predict, "r-")
plt.plot(X, y, "b.")
plt.axis([0, 2, 0, 15])
plt.show()

