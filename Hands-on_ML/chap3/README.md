# Training a Binary Classifier

* Binary classifiers distinguish between two classes.

> [...]

* Stochastic Gradient Descent (SGD) classifier.
    - This class has the advantage of being capable of handling very large datasets efficiently.
    - This is in part because SGD deals with training instances independently, one at a time (which also makes SGD well suited for online learning).

# Performance Measures

> Evaluating a classifier is often trickier than evaluating a regressor.

## Measuring Accuracy Using Cross-Validation

* **cross_val_score() function**: uses K-fold cross-validation, with three folds
    - Meaning: splits the training set into K-folds (in this cae, three)
        * Then making predictions and evaluating them on each fold using a model trained on the remaining folds.

**StratifiedKFold class**: performs stratified sampling to produce folds that contain a representative ratio of eah call. At each iteration the code creates a clone of the classifier, train that clone on the training folds, and makes prediction on the test fold. Then it counts the number of correct predictions and outputs the ratio of correct predictions.

> Notice that: Accuracy is generally not the preferred performance measure for classifiers, epecially when you're dealing with skewed datasets (i.e., when some classes are much more frequent than others).

## Confusion Matrix (CM)

> The general idea is to count the number of times intances of class A were classified as class B.

* Each row in a CM represents an actual class.
* Each column in a CM represents a predicted class.

<img src="https://miro.medium.com/max/1594/1*CPnO_bcdbE8FXTejQiV2dg.png" align="center" width="300">

* CM gives you a lot of information, but sometimes you may prefer a more concise metric.

### Precision

> Is the accuracy of positive predictons, i.e. what I know divided by what it is.

``` 
precision = TP/(TP+FP)
```

### Recall

* also called Sensitiviry or True Positive Rate (TRP)

> Is the ratio of positive instances that are correctly detected by the classifier, i.e. what I know divided by what I think it is.

``` 
recall = TP/(TP+FN)
```

### Precision and Recall

> It's often convenient to combine precision and recall into a single metric called F1-score.

* Is the non weighted harmonic mean of precision and recall.
    - Whereas the regular mean treats all values equally, the harmonic mean gives much more weight to low values.
    - The classifier will only get a high F1-score if both recall and precision are high.

``` 
F1-score = 1/(2(precision + recall)) = ... = TP/(TP+(FN+FP)/2)
```

* The F1-score favors classifiers that have similar precision and recall.
* This isn't always what you want:
    - Ex1: you trained a classifier to detect videos that're safe for kids.
        * You'd probably prefer a classifier that rejects many good videos (low recall), but keeps only safe ones (high precision)
        * rather than a classifier that has a much higher recall, but lets a few really bad videos show up in your product.
    - Ex2: You trained a classifier to detect shoplifters on surveillance images.
        * It's probably fine if your classifier has only 30% precision as long as it has 99% recall.

> Notice that: you can't have both. Increasing precision reduces recall and vice versa. This is called ther precision/recall tradeoff.

### Precision/Recall tradeoff

* By raising the decision threshold decreases recall.

<img src="https://miro.medium.com/max/1254/1*mQ6a-tiHstNaC3lTxSibkA.jpeg" align="center" width="600" heigth="300">

* Another way to select the best precision/recall tradeoff is to plot precision directly against recall.

<img src="https://i.imgur.com/7TIpZUb.png" align="center" width="600" heigth="300">

* The precision really starts to fall sharply around 80% recall.
* You'll probalby want to select a precision/recall tradeoff jsut before that drop. 
    - Of course the choice depends on the project.

> Notice that: a high-precision classifier isn't very useful it its recall is too low.

### The ROC Curve (Receiver Operating Characteristic)

* it's very similar to the precision/recall curve
    - but instead it plots the True Positive Rate (Recall) against the False Positive Rate (FPR).
    - FPR is the ratio of negatives instances that are incorrectly classified as positive.
        * FPR = 1 - TNR
        * TNR: true negative rate (a.k.a specificity), is the ratio of negative instances that are correctly classified as negative.
* ROC Curve plots sensitivity against 1-specificity

<img src="https://glassboxmedicine.files.wordpress.com/2019/02/roc-curve-v2.png?w=576" align="center" width="600" heigth="300">

* Once again there's a tradeoff.
    - The higher the recall (TPR), the more false positives (FPR) the classifier produces.
* One way to compare classifiers is to measure the area under the curve (AUC).
    - A perfect classifier will have ROC AUC equal to 1, whereas a purely random one will have ROC AUC equal to 1/2.

**When to use?**

* As a rule of thumb:
    - Precision/Recall curve: whenever the positive class is rare or when you care more about the false positives than the false negatives.
    - ROC curve: otherwise.

## Multiclass Classification

> Also called multinomial classifiers, can distinguish among more than two classes.

* Some algorithms are capable of hanndling multiple classes directly. e.g.:
    - Random Forest
    - Naive Bayes
* Others are strictly binary classifiers, e.g.:
    - Support Vector Machines 
    - Linear classifiers

> However, there're strategies to perform multiclass classification using multiplt binary classifier.

* For example: When you want to classify an image:
    - you get the decision score from each classifier for that image
    - select the class whose classifier outputs the highest score
* This is called the one-versus-all (OvA) stratey, a.k.a one-versus-the-rest.

* Another example: To train a binary classifier for every pair of digits (e.g., MNIST dataset)
    - one to distinguish 0s and 1s
    - another to distinguish 0s and 2s
    - another for 1s and 2s, and so on.
* This is called the one-versus-one (OvO) strategy.
    - If there're N classes, you'll need to train N(N-1)/2 classifiers.
    - The main advantage of OvO is that each classifier only needs to be trained on the part of the training set for the two classes that it must distinguish.

* E.g., SVM's scale poorly with the size of the training set &rightarrow; OvO is preferred since it's faster to train many classifiers on small training sets than few classifiers on larger training sets.
    - For most binary classification algorithms &rightarrow; OvA is preferred.

* Scikit-Learn detects when you try to use a binary classification algorithm for a multiclass classification task 
    - It automatically runs OvA &rightarrow; except for SVM which uses OvO.

## Error Analysis

> Analyzing the CM can often give you insights on ways to improve your classifier.

## Multilabel Classification

> In some cases you may want your classifier to output multiple classes for earch instance.

* For example: a face-recognition classifier
    - What should it do if it recognizes several people on the same picture?
        * It should attach one label per person it recognies, of course.
    - Picture that: the classifier has been trained to recognze three faces: Alice, Bob anc Charlie.
    - When it's shown a picture of Alice and Charlie, it should output [1, 0, 1]
        * Which means, "Alice yes, Bob no, Charlie yes".
* Such classification system that outputs multiple binary labels is called a multilabel classification system.

* There're many ways to evaluate a multilabel classifier
    - and selecting the right metric really on your project.
* One approach is to measure the F1-score for each individual label
    - then  simply compute the average score &rightarrow; this assumes that all labels are equally important, which may not be the case.

## Multioutput Classification

> It's simply a generalization of multilabel classification, where each label can be multicall (i.e., it can have more than two possible values).

# Keywords

* **Precision/Recall tradeoff:** Increasing precision reduces recall and vice versa.
