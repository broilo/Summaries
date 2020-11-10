import numpy as np
from sklearn.linear_model import Ridge

np.random.seed(42)

m = 20

X = 3*np.random.rand(m, 1)
y = 1+0.5*X+np.random.randn(m, 1)/1.5
X_new = np.linspace(0, 3, 100).reshape(100, 1)

ridge_reg = Ridge(alpha=1, solver="cholesky", random_state=42)
ridge_reg.fit(X, y)
ridge_reg.predict([[1.5]])
