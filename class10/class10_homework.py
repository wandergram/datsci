# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:57:28 2015

@author: alex
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
import statsmodels.formula.api as smf

# visualization
import seaborn as sns
import matplotlib.pyplot as plt



# read data into dataframe

data = pd.read_csv('yelp.csv', index_col=0)
data.head()

# explore relationship between cool, useful, funny votes, star ratings

data.groupby('stars').cool.describe()
data.groupby('stars').funny.describe()
data.groupby('stars').useful.describe()

# define features and response, fit regression line

sns.pairplot(data, x_vars=['cool','funny','useful'], y_vars='stars', size=6, aspect=0.7, kind='reg')

# explore relationship between features & response

sns.pairplot(data)

data.corr()

'''
The data suggest that bad reviews are much more likely to be voted useful and funny than good reviews.
Reviews marked "cool" have a positive correlation with star ratings. 
This makes intuitive sense - negative reviews are very useful, as they save people time and money,
and bad reviews can also often be very funny, especially if the reviewer is 
sarcastic. Positive reviews usually point out something special or unique
about the business, which will generate "cool" votes.
'''

# create a model using scikit learn
feature_cols = ['cool', 'funny', 'useful']
X = data[feature_cols]
y = data.stars

# instantiate and fit the model
linreg = LinearRegression()
linreg.fit(X, y)

# coefficients
print linreg.intercept_
print linreg.coef_
zip(feature_cols, linreg.coef_)

# create a model using statsmodels
lm = smf.ols(formula='stars ~ cool + funny + useful', data=data).fit()

# print p-values for coefficients
print lm.pvalues
# all p-values are very small

# print R squared with three features
lm = smf.ols(formula='stars ~ cool + funny + useful', data=data).fit()
print lm.rsquared
# 0.044

# print R squared with two features
lm = smf.ols(formula='stars ~ cool + funny', data=data).fit()
print lm.rsquared
# 0.027
# in both cases, R squared values are very small.

# train/test
def train_test_rmse(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    linreg = LinearRegression()
    linreg.fit(X_train, y_train)
    y_pred = linreg.predict(X_test)
    return np.sqrt(metrics.mean_squared_error(y_test, y_pred))

# use all three features to train
feature_cols = ['cool', 'funny', 'useful']
X = data[feature_cols]
train_test_rmse(X, y)
# 1.184

# exclude funny (one of the two features correlated with negative reviews)
feature_cols = ['cool', 'useful']
X = data[feature_cols]
train_test_rmse(X, y)
# 1.196 - slightly stronger model

# exclude useful
feature_cols = ['cool', 'funny']
X = data[feature_cols]
train_test_rmse(X, y)
# no substantial difference

# exclude cool?
feature_cols = ['funny', 'useful']
X = data[feature_cols]
train_test_rmse(X, y)
# 1.209
# only slightly stronger, but takes away the feature correlated with positive reviews.

# null RMSE
stars = ['stars']
X = data[stars]
train_test_rmse(X, y)
# RMSE of 7.79. 

# KNN

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)

feature_cols = ['cool', 'useful', 'funny']
X = data[feature_cols]

# store response vector in "y"
y = data.stars

# trying to predict using out of sample data
knn.predict([3, 20, 30])
# predicted 1 star.

# changing to knn = 5, more cool reviews
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
feature_cols = ['cool', 'useful', 'funny']
X = data[feature_cols]
y = data.stars
knn.predict([20, 5, 5])
# predicted 4 stars

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
X_new = [[6, 4, 10], [8, 1, 20]]
knn.predict(X_new)
knn.predict_proba(X_new)
knn.kneighbors([3, 20, 5])