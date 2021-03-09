# How to Deal with Imbalanced Datasets?

## First things first

The oposite of a pure balanced dataset is a highly imbalanced dataset. Unfortunately, these are quite common in the real world. An imbalanced dataset is a dataset where the number of data points per class (not necessarily just the target one) differs drastically, resulting in a heavily biased Machine Learning (ML) model that won't be able to learn the minority class. On the other hand when this imbalanced ratio isn't so heavily skewed toward one class, such dataset isn't that horrible, since many ML models can handle them [1].

Nevertheless, there are some extreme cases in which the class ratio is just wrong, for instance a dataset where 95% of the labels belongs to class A, while the remaining 5% fall under class B. This is pretty much what usually happens in cases as fraud detection [1]. In these extreme cases, the ideal course of action would be to collect more data. However, this is tipycally not feasible. Luckily, there's an alternative known as oversampling. Which basically means using the data we currently have to create more of it.

## The Metric Trap

One of the major problems when dealing with imbalanced datasets relates to the metrics used to evaluated the model. Simple metrics, *e.g.* accuracy score may be quite misleading. In a dataset with highly imbalanced classes, if the classifier always "predicts" the most common class without performing any analysis of the features, it will still result in a high accuracy rate, which is obviously illusory.

In this cases, the high accuracy rate is just an illusion. Therefore, the choice of the metric used in imbalanced datasets is extremely important. As an example, a more robust evaluation metric for and imbalanced datasets would be the Normalized Gini Coefficient, that ranges from approximately 0 for a perfect score, to 1 for a random guessing [2]. 

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIj3-f7pa4FgizyuITo9_vtMVPFpj6MA5rUg&usqp=CAU" align="center" width="300" heigth="200">

## Confusion Matrix



# References

1. [Handling Imbalanced Datasets with SMOTE in Python](https://www.kite.com/blog/python/smote-python-imbalanced-learn-for-oversampling/)

2. [Resampling strategies for imbalanced datasets](https://www.kaggle.com/rafjaa/resampling-strategies-for-imbalanced-datasets/notebook)

3. [Intuitive Explanation of the Gini Coefficient](https://theblog.github.io/post/gini-coefficient-intuitive-explanation/#:~:text=The%20Normalized%20Gini%20coefficient%20is,could%20give%20you%20a%20better)

