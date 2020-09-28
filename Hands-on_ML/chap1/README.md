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
    - k-Means
    - Hierarchical Cluster Analysis (HCA)
* Dimensionality Reduction
    - Principal Component Analysis (PCA)
    - Linear Discriminant Analysis (LDA)
* Visualization
    - t-distributed Stochastic Neighbor Embeding (t-SNE)
* Association Rule Learning
    - Apriori
    - Eclat

### Clustering: The algorithm tries to detect groups of similar patterns.

### Visualization: The algorith tries to plot the data while preserving as much as possible its structure, so you can understand how the data is organized and perhaps even identify unsuspected patterns.

### Dimensionality Reduction: The goal is to simplify the data without loosing too much information. E.g., by merging several correlated features into a single one.

### Association Rule Learning: The goal is to dig into large amounts of data and discover interesting relations between attributes.

# Instance-Based VS Model-Based Learning

One more way to categorize ML systems is by how they generalize. This basically means that that given a number of training examples, the system ned to be able to generalize to examples it has never seen before.

* Good performance in training isn't sufficient.
* The true goal is to perform well on new instances.

1. **Instance-based learning**

> The system learns the examples by heart, then generalizes to new cases using similarity measure.

2. **Model-based learning**

> To build a model from a set of examples, then use it to make predictions.

# Main Challenges of Machine Learning

 Two main things can go wrong: "bad algorithm" and "bad data".

 ## Examples of Bad Data:

 1. **Insufficient Quantity of Training Data**

 > It takes a lot of data for most ML algorithms to work properly. Even for simple problems you typically need thoudsands of examples, and for complex ones such as image or speech recognition you may need millions of examples (unless you can reuse parts of an existing model (transfer learning?))

 **To remember:** *[...] you may want to consider the tradeoff between spendeing time and money on algorithm development versus spending it on corpus development* - Michele Banko and Eric Brill.

2. **Nonrepresentative Training Data**

> In order to generalize well, it's crucial that your training data be representative of the new cases you want to generalize to. This is often harder than it sounds: 

* if the sample is too small, you'll have sample noise.
* but even very large samples can be nonrepresentative, you'll have sampling bias.

3. **Poor-Quality Data**

> It's often well worth the effort to spend time cleaning up your training data.

* If some instances are clearly outliers, it may help to simply discard them or try to fix the errors manually.
* If some instances are missing a fe feature, you must decide wheter you want to ignore this attribute altogether, ignore these instances, fill in the missing values, or train one model with the feature and another one without it.

4. **Irrelevant Features**

# Keywords: 

* **Training set:** Is the example that the system uses to learn.
* **Training instance (or sample):** Is the training example.
* **Data mining:** Applying ML techniques to dig into large amounts of data which  helps to discovering patterns hat were not immediately apparent.
* **Target:** Is the thing that you want to predict.
* **Features:** Is the characteristics that describes each data point.
* **Predictors:** Is the set of features.
* **Feature extraction:** Is the process of understanding the data set, fiding correlations among features and performing dimensionality reduction.
* **Similarity measure:** E.g., the total number of common words between two e-mails. Then, the system would flag an e-mail as spam if it has many words in common with a known spam e-mail.
* **Utility function (or fitness function):** It measures how good your model is.
* **Cost function:** It measures how bad your model is.
* **Inference:** To apply the model to make predictions o new cases.
* **Sample noise:** Nonrepresentative data as result of chance.
* **Sampling bias:** If the sampling method is flawed.
