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



# Keywords

* **Signals:** A piece of information fed to a ML system.
* **Pipeline:** Is a sequence of data processing components.
* **Tail heavy:** E.g., the histogram extend much farther to the right of the meadian than to the left.
* **Data snooping bias**: When you estimate the generalization error using the test set, your estimate will be too optimistic and you'll launch a system that won't perform as well as expected.
* **Stratified sampling:** The population is divided into homogeneous subgroups called *strata*, and the right number of instances is sampled from each stratum to guarantee that the test set is representative of the overall population.
