# Linear Regression

> More generally, a linear model makes a prediction by simply computing wieghted sum of the input features, plus a constant called the *bias term* (also called the *intercept term*).

```
yh = a0 + a1*x1 + a2*x2 + ... + an*xn
```
* yh is the predicted value
* n is the number of features
* xi is the i-th feature value
* aj is the j-th model parameter (including the bias term a0 and the feature weights a1,a2,...,an)

> Recall that: training a model means setting its parameter so that the model best fits the training set. Therefore, we first need a measure of how well (or poorly) the model fits the training data.

* Most common performance measure of a regression model is: RMSE.
    * Thus, to train a Linear Regression model, you need to find the value of "a" that minimizes the RMSE.
        * In practice, it's simples to minimize MSE than RMSE, and it leads to the same result.
        * The value that minimizes a function also minimizes its square root.

# Normal Equation

> It's a closed-form solution, i.e. a mathematical equation, that finds the value of "a" that minimizes the cost function.

# Computational Complexity

> 