import numpy as np
from sklearn.linear_model import ElasticNet

np.random.seed(42)

m = 20

X = 3*np.random.rand(m, 1)
y = 1+0.5*X+np.random.randn(m, 1)/1.5
X_new = np.linspace(0, 3, 100).reshape(100, 1)

elastic_net = ElasticNet(alpha=0.1, l1_ratio=0.5)
elastic_net.fit(X, y)
elastic_net.predict([[1.5]])
