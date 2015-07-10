# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:42:57 2015

@author: alex
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics

data = pd.read_csv('titanic.csv', index_col=0)
data.head()

feature_cols = ['Pclass', 'Parch']
X = data[feature_cols]
y = data.Survived

'''
def train_test_rmse(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    logreg = LogisticRegression()
    logreg.fit(X_train, y_train)
    y_pred = logreg.predict(X_test)
    return np.sqrt(metrics.mean_squared_error(y_test, y_pred))
'''


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

logreg = LogisticRegression(C=1e9)
logreg.fit(X_train, y_train)

zip(feature_cols, logreg.coef_[0])

print logreg.predict(X) 
print logreg.intercept_
print logreg.coef_

logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

print metrics.accuracy_score(y_test, y_pred)

data['null'] = data.Survived.mean()




