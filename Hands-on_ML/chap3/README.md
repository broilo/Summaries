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

## Confusion Matrix



# Keywords
