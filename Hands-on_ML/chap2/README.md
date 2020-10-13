# Working with Real Data

Here are a few places to look for data set:

* Popular open data repositories:
    - [UC Irvine Machine Learning Repository](http://archive.ics.uci.edu/ml/index.php)
    - [Kaggle datasets](https://www.kaggle.com/datasets)
    - [Amazon’s AWS datasets](https://registry.opendata.aws/)
* Meta portals (they list open data repositories): 
    - http://dataportals.org/
    - http://opendatamonitor.eu/
    - http://quandl.com/
* Other pages listing many popular open data repositories: 
    - [Wikipedia’s list of Machine Learning datasets](https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research)
    - [Quora.com question](https://www.quora.com/Where-can-I-find-large-datasets-open-to-the-public)
    - [Datasets subreddit](https://www.reddit.com/r/datasets/)

# Look at the Big Picture

This chapter will use the [California Housing Prices data set from the StatLib repository](https://raw.githubusercontent.com/ageron/handson-ml2/master/).

## Frame the Problem

> First question: What's exactly the business objective and how does the company expect to use and benefit from this model?

* To build a model probably isn't the end goal.
* This first question will determine:
    - how to frame the problem.
    - what algorithm to select.
    - what performance measure can be used to evaluate the model.
    - how much effort should be spent tweaking it.

> Second question: What the current solution (if any) looks like?

* It will often give you: 
    - reference performance
    - insights on how to solve the problem

## Select Performance Measure

### Root Mean Square Error (RMSE)

* A typical performance measure for regression problems.
* It measures the standard deviations of the errors the system makes in its predictions.
* Is the cost function measured on the set of examples using your hypothesis.

### Mean Absolute Error (MAE)

* Mostly used when there are many outliers in the data set.

## Check the Assumptions

> It is a good practice to list and verify the assumptions that were made so far (by you and the team).

## Get the Data

[It's time to get our handas dirty!](https://github.com/ageron/handson-ml2/blob/master/02_end_to_end_machine_learning_project.ipynb)

### Create a Test Set

> It seems strange to voluntarily set aside part of the data. After all, you should learn a whole lot more about it before you decide which algorithms to use, right? 

> That's true, but if we look at the test set, we'd probably stumble upon some seemingly interesting pattern. Most probably we'd end up using it to select a particular ML model. 

* This is associated with data snooping bias.

## Prepare the Data for ML Algorithms

### Data cleaning

* get rid of missing values.
* Get rid of the whole attribute.
* Set the values to some value (zero, the mean, the median, etc.).

## Scikit-Learn main design principles

* Consistency: All objects share a consistent and simple interface.
    - Estimators: Any object that can estimate some parameters based on a dataset. Any other parameter needed to guide the estimation is considered a hyperparameter.
    - Transformers: Some estimators can also transform a dataset.
    - Predictors: Some estimators are capable of making predictions.
* Inspection: All the estimator's hyperparameters are accessible directly via public instance variables, and all the estimator's learned parameter are also accessible via public instance variables with an underscore suffix.
* Nonproliferation of classes: Datasets are represented as NumPy arrays or SciPy sparse matrices, instead of homemade classes. Hyperparameters are just regular Python strings or numbers.
* Composition: Existing building blocks are reused as much as possible. E.g., it's ease to create a Pipeline estimator from an arbitrary sequence of transformers followed by a final estimator.
* Sensible defaults: Scikit-Learn provides reasonable default values for most parameters, making easy to create a baseline working system quickly.

## Handling Text and Categorical Attributes

* Convert labels to numbers.
    - Label Encoding: each class is mapped into a number.
    - One-Hot Encoding: It's a binary category where one attribute is equal to 1 when the category is "A" and 0 otherwise, another attibute is equal to 1 when is "B" and 0 otherwise, and so on. So, it's an encoder to convert integer categorical values into one-hot vectors, because only one attibute will be equal to 1 (hot), while the others will be 0 (cold).
        * Notice that the outpu is a SciPy sparse matrix, instead of a NumPy array.

## Feature Scaling

* One of the most important transformations is Feature Scaling.
    - In genereal, ML algorithms don't perform well when the input numerical attributes have very different scales. 
    - Notice that scaling the target values is generally not required.

> There're two common ways to get all attributes to have the same scale:

### Min-max scaling (many people call this normalization)

* Values are shifted and rescaled so that they end up ranging from 0 to 1.
* How it's done: Substract the min value from each value and divide it by the max minus the min.

### Standardization

* First it subtracts the mean value, and then it divides by the variance so that the resulting distribution has unit variance.
* Doesn't bound values to a specific range.
* Is much less affected by outliers.

## Transformation Pipelines

> There're many data transformation steps that need to be executed in the right order, 

* The Pipeline contructor from Sckit-Learn takes a list/estimator pairs defining a sequence of steps.

## Select and Train a Model

### Training and Evaluation on the Training Set

* **Underfitting** the data: when it happens, it can mean that the features don't provide enough information to make good predictions, or that the model isn't powerful enough.
    - The main ways to fix it are:
        * To select a more powerful model.
        * To feed the training algorithm with better features.
        * To reduce the constraints on the model.

* **Overfitting** the data: when it happens, it can mean that the model are too complex that it's able to classify/fit/predict even outliers. 
    - The main ways to fix it are:
        * To reduce the number of features.
        * To simplify the model.
        * To reduce the noise in the training data.

### Better Evaluation Using Cross-Validation

 * **k-fold cross-validation**: it randomly splits the training set into 10 distinct subsets called folds, then it trains and evaluates the classifier 10times, picking a different fold for evaluation every time and training on the other 9 folds.
    - The result is an array containing the 10 evaluation scores.

> **Obs**: Sckit-Learn cross-validation features expect an utility function (greater is better) rather than a cost function (lower is better), so the scoring function is actually the opposite of the MSE (i.e., a negative value), which explains why the code computes -scores before calculating the square root.

# Keywords

* **Signals:** A piece of information fed to a ML system.
* **Pipeline:** Is a sequence of data processing components.
* **Tail heavy:** E.g., the histogram extend much farther to the right of the meadian than to the left.
* **Data snooping bias**: When you estimate the generalization error using the test set, your estimate will be too optimistic and you'll launch a system that won't perform as well as expected.
* **Stratified sampling:** The population is divided into homogeneous subgroups called *strata*, and the right number of instances is sampled from each stratum to guarantee that the test set is representative of the overall population.
