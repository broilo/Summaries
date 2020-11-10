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
    - It measures the local gradient of the error function with regards to the parameter vector, and it goes in the direction of descending gradient. 
        * Once the gradient is zero, you've reached a minimum!

<img src="https://kharshit.github.io/img/gradient_descent_demystified.png" align="center" width="400" heigth="200">

* You start by filling the parameter vector with random values (random initialization)
    - and then you improve it gradually, taking one baby step at a time
    - each step attempting to decrease the cost function, until the algorithm converges to a minimum.

## The size of the steps

* It's an important parameter in Gradient Descent.
* And it's determined by the learning rate hyperparameter.
    - Too small: then the algorithm will have to go through mny iterations to converge, 
        * and consequently will take a long time.
    - Too large: then you might jump across the valley and end up on the other side, possibly even higher than you were before.
        * This could make the algorithm to diverge and failing to find a good solution.

<img src="https://cdn-images-1.medium.com/max/1000/1*n79s9gvd0E8ALe9dLUEKAw.png" align="center" width="500" heigth="300">

<img src="https://miro.medium.com/max/2670/1*vCjuDIofrymzImk1X9z58Q.png" align="center" width="500" heigth="300">

* Not all cost functions look like nice regular bowls:

<img src="https://pic1.zhimg.com/80/v2-6c5e20f498158c39ad76edaeb04e763a_1440w.jpg" align="center" width="500" heigth="300">

* The MSE cost function for a Linear Regression model happens to be a convex function.

    Which means that there're not any local minima, just one global minimum.

* In fact, the cost function has the shape of a bowl, but it can be an elongated bowl if the features have very different scales.
* Therefore, when using Gradient Descent, you should ensure that all features have a similar scale (e.g., using Scikit-Learn's StandardScaler class), or else it'll take much longer to converge.

* Training a model means searching for a combination of model parameters that minimizes a cost function (over the training set).
    - It's a search in the model's parameter space.
        * The more parameters a model has, the more dimensions this space has, and harder the search is.

## Batch Gradient Descent

> To implement Gradient Descent, you need to compute the gradient of the cost function with regards to each model parameter.

* You need to calculate how much the cost function will change if you change the model parameter just a little bit.
    - This is called partial derivative.
* Notice that the Gradient vector of the cost function involves calculations over the full training set, at each Gradient Descent step.
    - This is why the algorithm is called Batch Gradient Descent
    - It uses the whole batch of training data at every step.
        * As a result, it's terribly slow on very large training sets.

* To find a good learning rate:
    - You can use grid search
        * limit the number of iterations so that the grid search can eliminate models that take too long to converge.

### How to set the the number of iteration?

* If it's too low, you'll still be far away from the optimal solution when the algorithm stops.
* If it's too high, you'll waste time while the model parameters don't cahnge anymore.

### A simple solution

* To set a very large number of iterations
    - but to interrupts the algorithm when the gradient vector becomes tiny.
    - That is, when its norm becomes smaller than a tiny number called the tolerance.
        * This happens when the Gradient Descent has almost reached the minimum.

> **The manin problem:** is the fact that it uses the whole training set to compute the gradients at every step, which makes it very slow when the training set is large.

## Stochastic Gradient Descent

> It just picks a random instance in the training set at every step and computes the gradients based only on that single instance.

* This makes the algorithm much faster since it has very little data to manipulate at every iteration.
* It also makes it possible to train on huge training sets, since only one instance needs to be in memory at each iteration.
    - SGD can be implemented as an out-of-core algorithm

* Due to its stochastic (random) nature, this algorithm is much less regular than BGD.
    - instead of gently decreasing until it reaches the minimum, the cost function will bounce up and down, decreasing only on average.
* Over time it'll end up very close to the minimum, 
    - but once it gets there it'll continue to bounce around.
* When tha algorithm stops, the final parameter values are good, but not optimal.

* When the cost function is very irregular:
    - this can actually help the algorithm to jump out of a local minima
* SGD has a better chance of finding the global minimum than BGD does.

### Randomness

* Is good: to escape from local optima.
* Is bad: because it means the algorithm can never settle at the minimum.

> One solution: is to gradually reduce the learning rate.

* Simulated annealing process, see Keywords.

* If the learning rate is reduced:
    - too quickly, you may get stuck in a local minimum, or even end up frozen halhway to the minimum,
    - too slowly, you may jump arund the minimum for a long time and end up with a supoptimal solution if you halt training too early.

## Mini-batch Gradient Descent

> Computes the gradients on small random sets of instances called mini-batches.

* The algorithm's progress in parameter space is less erratic than with SGD, 
    - especially with fairly large mini-batches.
* It'll end up walking around a bit clores to the minimum than SGD.
* However, it may be harder to escape from local minima.

# Polynomial Regression

* You can fit actually use a linear model to fit nonlinear data.
    - A simple way to do this is to add powers of each feature as new features, than train a linear model on this extended set of features.
    - This is called Polynomial Regression.

* A way to tell if the model is too simple or too complex is to check if the model is underfitting or overfitting.
    - Which means, if the model performs poorly on both training ans testing or if the model performs well on the training but generalizes poorly.
* Another way is to look at the learning curves.

* One way to improve an overfitting model is to feed it more training data until the validation error reaches the training error.

# The Bias/Variance Tradeoff

> The model's generalization error can be expressed as the sum of three very different errors.

* Bias:
    - This part of the generalization error is due to wrong assumptions. 
    - A high-bias model is most likely to underfit the training data.

* Variance:
    - Is due to the model's excessive sensitivity to small variations in the training data.
    - A model with many degrees of freedom, such as a high-degree polynomial model, is likely to have high variance, and thus to overfit the training data.

* Irreducible error:
    - Is due to the noisiness of the data itself.
    - The only way to reduce this part of the error is to clean up the data:
        1. fix data sources
        1. remove outliers
        1. ...

### One one hand: 

* Increasing a model's complexity will typically increase its variance and reduce its bias.

### On the other hand:

* Reducing a model's complexity increases its bias and reduces its variance.

> This is why it's called a tradeoff.

## Ridge Regression (a.k.a. Tikhonov regularization)

> Is a regularized version of Linear Regression.

* A regularization term is added to the cost function.
    - This forces the learning algorithm to not just fit the data but also keep the model weigths as small as possible.
* Notice that the regularization term should only be added to the ost function during training.
    - Once the model is trained, you want to evaluate the model's performance using the unregularized performance measure.

* The hyperparameter controls how much you want to regularize the model. 
    - Is this hyperparameter is zero, then Ridge Regularization is just Linear Regression.
    - If it's very lage, then all weights end up very close to zero and the result is a flat line going through the data's mean.

> It's important to scale the data, most regularized models are sensitive to the scale of the input features.

## Lasso Regression

> Just like Ridge, it adds a regularization term to the cost function.

# Keywords

* **Convergence rate:** When the cost function is convex and its slope doesn't change abruptly, it can be shown that the Batch Gradient Descent with a fixed learning rate has a convergence rate of O(1/iterations). In other words, if you divide the tolerance by 10 (to have a more precise solution), then the algorithm will have to run 10 times more iterations.
* **Simulated annealing:** E.g., the steps start out large (which helps make quick progress and escape local minima), then get smaller and smaller, allowing the algorithm to settle at the global minimum.
* **Learning schedule:** Is the function that determines the learning rate at each iteration.
* **Learning curver:** These are plots of the model's performance on the training set and the validation set as a function of the training set size.
* **Bias:** It's a "measure" of how simple or restricted is the model.
* **Variance:** It's a "measure" of the variability of the model.
