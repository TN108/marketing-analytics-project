Conversion Prediction Model Evaluation

Objective

The model predicts whether a marketing interaction will result in an order:

0: no conversion

1: conversion

The source is the silver_marketing_interactions table. Unbiased test predictions are written to gold_conversion_predictions.

Leakage-safe features

The model uses information available before the purchase decision:

Customer age

Customer gender

Customer region

Product category

Unit price

Marketing channel

Device type

Discount percentage

The following outcome-related columns are excluded: clicks, website visits, orders, units sold, revenue, and the target itself. Revenue, orders, and units sold would reveal that a conversion had already occurred.

Data splitting

The data is divided into training and test sets using an 80/20 stratified split. The training portion is divided again into subtraining and validation sets. The validation set is used for imbalance experiments and threshold selection. The test set remains untouched until the final evaluation.

This structure prevents test-set leakage and provides an unbiased final performance estimate.

Feature preparation

Categorical features are transformed with one-hot encoding. Numerical features are standardized. Both operations are kept inside the model pipeline so that preprocessing parameters are learned only from training data.

Class imbalance

Only 169 of 10,000 interactions converted, giving a positive rate of approximately 1.69%. A model predicting every row as a non-conversion would therefore obtain high accuracy while finding no customers who convert.

Two imbalance strategies were investigated:

Class weighting, which increased the importance of conversions but produced many false positives.

Classification-threshold tuning, which retained the baseline probability ranking and selected the threshold using validation F1.

The selected validation threshold was 0.05 instead of the default 0.50.

Final test results

Metric

Result

Threshold

0.050

True positives

5

False positives

23

False negatives

29

True negatives

1,943

Accuracy

0.9740

Precision

0.1786

Recall

0.1471

F1 score

0.1613

ROC-AUC

0.7374

PR-AUC

0.0727

Interpretation

The model correctly identified 5 of the 34 conversions in the untouched test set. It made 28 positive predictions, of which 5 were correct. Thus, its precision was 17.86% and its recall was 14.71%.

The ROC-AUC of 0.7374 indicates moderate ability to rank converters above non-converters. The lower PR-AUC reflects the difficulty of the highly imbalanced problem. Accuracy is not the principal decision metric because the negative class dominates the dataset.

The model is useful as a baseline, but its low recall shows that demographic, product, channel, device, price, and discount features do not capture every factor that drives conversion. Future versions could add leakage-safe behavioral history, customer recency and frequency, prior campaign engagement, seasonality, and customer-product affinity.

Output table

gold_conversion_predictions contains the untouched test-set predictions, including:

Available business identifiers

Input features

Actual conversion label

Predicted conversion label

Conversion probability

Classification threshold

Model name

Dataset split

Prediction timestamp