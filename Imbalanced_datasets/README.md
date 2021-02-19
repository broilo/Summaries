# How to Deal with Imbalanced Datasets?

## The Metric Trap

One of the major problems when dealing with unbalanced datasets relates to the metrics used to evaluated the model. Simple metrics, *e.g.* accuracy_score may be quite misleading. In a dataset with highly unbalanced classes, if the classifier always "predicts" the most common class without performing any analysis of the features, it will still result in a high accuracy rate, which is obviously illusory.

* [Normalized Gini Coefficient](https://theblog.github.io/post/gini-coefficient-intuitive-explanation/#:~:text=The%20Normalized%20Gini%20coefficient%20is,could%20give%20you%20a%20better): 
    - is a more robust metric for imbalanced datasets, that ranges from approximately 0 for random guessing, to approximately 0.5 for a perfect score.

<img src="https://xpic.x-mol.com/20191201%2F10.1038_s41598-019-54288-7.png" align="center" width="400" heigth="200">

## Confusion Matrix

# References

1. [Resampling strategies for imbalanced datasets](https://www.kaggle.com/rafjaa/resampling-strategies-for-imbalanced-datasets/notebook)

1. [Intuitive Explanation of the Gini Coefficient](https://theblog.github.io/post/gini-coefficient-intuitive-explanation/#:~:text=The%20Normalized%20Gini%20coefficient%20is,could%20give%20you%20a%20better)