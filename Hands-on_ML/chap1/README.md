# What is Machine Learning?

> *"Machine Learning is a thing labeler. Is an approach to making lots of small decisions with data"* - [Cassie Kozyrkov](https://www.youtube.com/watch?v=L1AiQwxkX7A)

Differently from traditional programming, in ML is the programmer's task to feeding examples into the system and it's the ML algorithm's job to stitch the recipe together out of the examples.
 
Example: A spam filter based on ML techniques automatically learns which words and phrases are good predictors of spam by detecting unusually frequent patterns of words in the spam examples compared to the ham examples.

> Machine Learning can help humans learn!

# Types of Machine Learning Systems

## Most Common ones

1. **Supervised**

> *"You tell the system what the correct output is that goes with an input"* - [Cassie Kozyrkov](https://www.youtube.com/watch?v=mLFzvzuA5LM)

In supervised learning, the training data you feed to the algorithm includes the desired solution. Therefore, the algorithm create a prediction function and applies what he learned in an entirely new and unknown data set. 

Examples of Supervised Learning Algorithms (most common):
* k-Nearest Neighbors
* Linear Regression
* Logistic Regression
* Support Vector Machines (SVMs)
* Decision Trees and Random Forests

2. **Unsupervised**

> *"You don't give any lables in advance and just tell the system to put similar things together"* - [Cassie Kozyrkov](https://www.youtube.com/watch?v=mLFzvzuA5LM)

In unsupervised learning, the training data is unlabeled. Therefore, the system isn't aiming to find the correct answer, but to exploring the data and searching for some pattern. Basically, the system tries to learn without a teacher.

Examples of Unsupervised Learning Algorithms (most common):
* Clustering
    * k-Means
    * Hierarchical Cluster Analysis (HCA)
* Dimensionality Reduction
    * Principal Component Analysis (PCA)
    * Linear Discriminant Analysis (LDA)
* Visualization
    * t-distributed Stochastic Neighbor Embeding (t-SNE)
* Association Rule Learning
    * Apriori
    * Eclat

### Clustering: The algorithm tries to detect groups of similar patterns.

### Visualization: The algorith tries to plot the data while preserving as much as possible its structure, so you can understand how the data is organized and perhaps even identify unsuspected patterns.

### Dimensionality Reduction: The goal is to simplify the data without loosing too much information. E.g., by merging several correlated features into a single one.

### Association Rule Learning: The goal is to dig into large amounts of data and discover interesting relations between attributes.


 # Keywords: 
 * Training set: Is the example that the system uses to learn.
 * Training instance (or sample): Is the training example.
 * Data mining: Applying ML techniques to dig into large amounts of data which  helps to discovering patterns hat were not immediately apparent.
 * Target: Is the thing that you want to predict.
 * Features: Is the characteristics that describes each data point.
 * Predictors: Is the set of features.
 * Feature extraction: Is the process of understanding the data set, fiding correlations among features and performing dimensionality reduction.
