# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 21:43:32 2015

@author: alex
"""
'''
Tasks:
Bonus: Turn this into a 5-class classification problem by predicting the star rating using the original DataFrame (from step 1). Calculate the accuracy and print the confusion matrix. Comment on the results.
'''

# Part 1.
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split

# read data into dataframe
data = pd.read_csv('yelp.csv', index_col=0)
data.head()

# Create a new dataframe that contains only the 5-star and 1-star reviews.
# I know that there's a much easier way to do this; for whatever reason, I blanked on it! 
df = data[data.stars != 2] 
df.head()
df.shape

df2 = df[df.stars != 3]
df2.shape

df3 = df2[df2.stars != 4]
df3.head()
df3.shape
df3.stars.describe() # checked everything to make sure it makes sense 

# Mapped fives and ones to ones and zeros. Moved this code up from the ROC/AUC score section.
df3['stars'] = df3.stars.map({5:1, 1:0})
df3.head() #check to make sure it works

# Split dataframe into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(df3.text, df3.stars, random_state=1)
X_train.shape
X_test.shape

# Use CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(decode_error = 'ignore') # found decode_error = ignore on stackoverflow, seems to work
vect.fit(X_train)
vect.get_feature_names()

# This may be superfluous...
vect2 = CountVectorizer(decode_error = 'ignore')
vect2.fit(X_test)
vect2.get_feature_names()

# Create document-term matrices
# I am not entirely sure on the difference between fit_transform and transform here.
# They seem to produce different results?
train_dtm = vect.fit_transform(X_train)
train_dtm

test_dtm = vect.transform(X_test)
test_dtm

# Use Naive Bayes to predict stars
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(train_dtm, y_train)

y_pred_class = nb.predict(test_dtm)

# Calculate accuracy
from sklearn import metrics
metrics.accuracy_score(y_test, y_pred_class) # 92%

# Print confusion matrix
metrics.confusion_matrix(y_test, y_pred_class)
# Sensitivity
# TP / TP + FN

from __future__ import division 
# in Python 2.x this has to be added otherwise it will truncate the float
126 / (126 + 58) # 0.6847

# Specificity
# TN / TN + FP
813 / (813 + 25) # 0.9701

y_pred_prob = nb.predict_proba(test_dtm)[:, 1]
print y_pred_prob # to check
metrics.roc_auc_score(y_test, y_pred_prob) # AUC score 94%

# Plot ROC curve
import matplotlib.pyplot as plt

fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred_prob)
plt.plot(fpr, tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('false positive rate')
plt.ylabel('true positive rate - sensitivity')

# false positives
X_test[y_test < y_pred_class]
# contains text such as "great example" (of what not to do), "strongly recommend" (you stay away)

# false negatives
X_test[y_test > y_pred_class]
# contains text such as "I would rather not", "poor customer service" (regarding prior reviews), "could not promise", "nasty virus", etc. 

# Part 2. Running the same on the original dataframe.
X_train, X_test, y_train, y_test = train_test_split(data.text, data.stars, random_state=1)
X_train.shape
X_test.shape

vect = CountVectorizer(decode_error = 'ignore') # found decode_error = ignore on stackoverflow, seems to work
vect.fit(X_train)
vect.get_feature_names()

# This is still probably superfluous...
vect2 = CountVectorizer(decode_error = 'ignore')
vect2.fit(X_test)
vect2.get_feature_names()

train_dtm = vect.fit_transform(X_train)
train_dtm

test_dtm = vect.transform(X_test)
test_dtm

nb = MultinomialNB()
nb.fit(train_dtm, y_train)

y_pred_class = nb.predict(test_dtm)

metrics.accuracy_score(y_test, y_pred_class) # accuracy is 47% - much lower than previously with only two outcomes. 
# The lower accuracy score probably has to do with there being relatively little difference between the
# words people use when giving 1-2, 2-3, 3-4 and 4-5 star reviews. The difference between 1 and 5 star reviews
# is typically much more stark.
