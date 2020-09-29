# What is Machine Learning?

> *"Machine Learning is a thing labeler. Is an approach to making lots of small decisions with data"* - [Cassie Kozyrkov](https://www.youtube.com/watch?v=L1AiQwxkX7A)

Differently from traditional programming, in ML is the programmer's task to feeding examples into the system and it's the ML algorithm's job to stitch the recipe together out of the examples.

Machine Learning is about making machines get better at some task by learning from data, instead of having to explicitly code rules.

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

> "Trash in, trash out"

* A critical part of the success of a ML project is coming up with a good set of features to train on.
* The quality of your results is intrinsically connected to the quality of your available data set.
* Feature engineering: 
    - Feature selection
    - Feature extraction
    - Creating new features

## Examples of Bad Algorithms:

1. **Overfitting the Training Data**

> Is the process of overgeneralizing, something that we humans do all too often.

* It means that the model performs well on the training data, but it doesn't generalize well on test.
* Overfitting happens when the model is too complex relative to the amount and noisiness of the training data.
* Possibel solutions (Regularization):
    - To simplify the model by selecting fewer parameters
        * by reducing the number of attributes in the training data
        * by constraining the model
    - To gather more training data.
    - To reduce the noise in the training data
        * by fixing data errors
        * by removing outliers

> You want to find the right balance between fitting the data perfectly and keeping the model simple enough to ensure that it will generalize well.

* The amount of regularization to apply during learning can be controlled by a hyperparameter.
    * Tuning hyperparameters is an important part of building a ML system.

2. **Underfitting the Training Data**

> The model is too simple to learn the undelying structure of the data.

* Reality is just more complex than the model, so its predictions are bound to be inaccurate, even on the training set.
* Possible solutions:
    * To select a more powerful model, with more parameters.
    * Too feed beter features to the learning algorithm (feature engineering).
    * To reduce the constraints on the model.

# Testing and Validating

* To split the data into two sets:
    * Training set
    * Test set
    * Evaluating the model on the test set gives you an estimation of the generalization error.
        * This value tells you how well the model will perform on instances it has never seen before.

> A common process to have a second holdout set called the validation set.
* You train multiple models with various hyperparameters using the training set.
* You select the model and hyperparameters that perform best on the validation set.
* The, you run the model on the test set, one time only, to get an estimate of the generalization error.

> A very common technique is to use cross-validation.

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
* **Feature engineering:** Is the process associated with "problem understanding" task and to catching the importance and essence from the features.
* **Feature selection:** To select the most useful features to train on among the whole available features.
* **Feature extraction:** To combine existing features to produce a more useful one. 
* **Creating new features:** To create new features by gathering new data.
* **Regularization:** Constraining a model to make it simpler and reduce the risk of overfitting.
* **Hyperparameter:** Is a parameter of the learning algorithm (not from the model itself).
* **Training set:** Where you train the model.
* **Test set:** Where you apply the model.
* **Generalization Error:** The error rate on new cases.
* **Cross-validation:** The training set is splited into complementary subsets, and each model is trained against a different combination of these subsets and validade against the remaining parts. Once the model type and hyperparameters have been selected, a final model is trained using these hyperparameters on the full training set, and the generalized error is measured on the test set.

# Exercises

1. How would you define Machine Learning?
    * ML is all about feeding the system with examples so that the system, not the programmer, learns from these example and at the end turns out to be able to find a recipe based on it. The learning process in ML models simply means to get better at some task and evaluating the system performance.

2. Can you name four types of problems where it shines?
    * ML is perhaps the best approach so far to solve complex problems where there isn't a close solution. But most of all, ML can help humans to learn, e.g. a huge data set where at first glance doesn't seem to have any pattern at all, to replace the divine inspiration of a programmer to simply build a recipe based on what de ML model learned from the data, build systems that can recommend thing based on our behavior and perform imagae and speech recognition.

3. What is a labeled training set?
    * Is a set of examples that contains the desired solutions. 

4. What are the two most common supervised tasks?
    * Classification and Regression.

5. Can you name four common unsupervised tasks?
    * Clustering, visualization, dimensionaltity reduction and association learning.

6. What type of Machine Learning algorithm would you use to allow a robot to walk in various unknown terrains?
    * Reinforcement learning, because it would reward or not the system based on the best strategy (policy) of learning.

7. What type of algorithm would you use to segment your customers into multiple groups?
    * It dependes, if you don't have any clue regarding the customers, then I'd say a clustering algorithm, which is an unsupervised ML task. However, if you already have some knowledge regarding the problem, then I'd go with a classification algorithm, which is supervised ML task.

8. Would you frame the problem of spam detection as a supervised learning problem or an unsupervised learning problem?
    * Supervided learning problem, because the spam filter is previously trained based on a set of known mesages classified as spam.

9. What is an online learning system?
    * Is a system where the training process is performed incrementally by feeding it with data instances sequentially, either individually or by small groups (mini-batches).

10. What is out-of-core learning?
    * Is a type of online learning applied to training systems on huge data sets that can't fit in one machine's main memory.

11. What type of learning algorithm relies on a similarity measure to make predictions?
    * Instance-based learning, because the system learn by heart. Therefore, when given a new instance, it uses similarity measure to find the most similar learned instances and uses them to make predictions.

12. What is the difference between a model parameter and a learning algorithm’s hyperparameter?
    * A model parameter is an intrinsic feature of the model that you may or may not consider. A hyperparameter is a parameter associated with the algorithm, i.e. the classifier itself, which is used to fine-tune the model.

13. What do model-based learning algorithms search for? What is the most common strategy they use to succeed? How do they make predictions?
    * They search for an optimal value for the model parameter such that the model might generalize well on new instances. Usually is training the system by minimizing the cost-function that measures how bad the system is at making predictions on the training data, plus a penalty for model complexity, if the model is regularized. To make predictions, we feed the new instance features into the model prediction function, by using the parameter values found by the learning algorithm.

14. Can you name four of the main challenges in Machine Learning?
    * Lack of and poor data quality, nonrepresentative training data, simple models that underfit in training and complex ones that overfit and don't generalize.

15. If your model performs great on the training data but generalizes poorly to new instances, what is happening? Can you name three possible solutions?
    * Overtraining. Reduce model complexity, gather more training data, reduce noise/outliers in the training set.

16. What is a test set and why would you want to use it?
    * A test set is the data where the ML model will be evaluated its performance related to generalization and estimated the generalization error. It should be used because this is inform how good/bad is the ML model before it's lunched in production.

17. What is the purpose of a validation set?
    * Is to fine-tune the ML model before it's tested into "real" data.

18. What can go wrong if you tune hyperparameters using the test set?
    * Well, this is sort of the problem known as Data Leakage. But, most probably the model will overfit the test and won't perform well on new data. 

19. What is cross-validation and why would you prefer it to a validation set?
    * Is the process of splitting the training data into complementary subsets so that the model is trained against a different combination of these subsets and then validated against the remaining parts.