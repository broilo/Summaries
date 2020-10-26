# Linear Regression

> More generally, a linear model makes a prediction by simply computing wieghted sum of the input features, plus a constant called the *bias term* (also called the *intercept term*).

``` 
yh = a0 + a1*x1 + a2*x2 + ... + an*xn
```

* yh is the predicted value
* n is the number of features
* xi is the i-th feature value
* aj is the j-th model parameter (including the bias term a0 and the feature weights a1, a2, ..., an)

> Recall that: training a model means setting its parameter so that the model best fits the training set. Therefore, we first need a measure of how well (or poorly) the model fits the training data.

* Most common performance measure of a regression model is: RMSE.
    - Thus, to train a Linear Regression model, you need to find the value of "a" that minimizes the RMSE.
        * In practice, it's simples to minimize MSE than RMSE, and it leads to the same result.
        * The value that minimizes a function also minimizes its square root.

# Normal Equation

> It's a closed-form solution, i.e. a mathematical equation, that finds the value of "a" that minimizes the cost function.

# Computational Complexity

> The normal equation computes the inverse of X^{T}X, which is an n x n matrix and n is the number of features.

* The computational complexity of inverting such a matrix is tipically O(n^3)
* If you double the number of features, you multiply the computation time by roughly 2^3 = 8.
* On the bright side, this equation is linear with regards to the number of instances in the training set.
    - So it handles large training sets efficiently.
        * Provided they can fit in memory.
* Once you have trained your Linear Regression model, predictions are very fast.
    - The computational complexity is linear with regards both the number of instances you want to make predictions on and the number of features.
        * Making predictions on twice as many instances (or twice as mane features) will jsut take roughly twice as much time.

# Gradient Descent

> Is a very generic optimization algorithm capable of finding optimal solutions to a wide range of problems.

* The general idea: to tweak parameters iteratively in order to minimize a cost function.
    * It measures the local gradient of the error function with regards to the parameter vector, and it goes in the direction of descending gradient. 
        * Once the gradient is zero, you've reached a minimum!

<img src="https://kharshit.github.io/img/gradient_descent_demystified.png" align="center" width="600" heigth="300">
