# Training a Binary Classifier

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

``` 
TN | FP
--------
FN | TP
```

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
    * Ex2: You trained a classifier to detect shoplifters on surveillance images.
        * It's probably fine if your classifier has only 30% precision as long as it has 99% recall.

> Notice that: you can't have both. Increasing precision reduces recall and vice versa. This is called ther precision/recall tradeoff.

### Precision/Recall tradeoff

<img src="https://miro.medium.com/max/1254/1*mQ6a-tiHstNaC3lTxSibkA.jpeg" align="right" width="300">


# Keywords
**Precision/Recall tradeoff:** Increasing precision reduces recall and vice versa.