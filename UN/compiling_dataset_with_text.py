# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 22:05:54 2015

@author: alex
"""

import glob

# working dir: meeting_records_clean_final
# read all files in directory into a list, where 1 file = 1 list element
list_of_meetings = []
for filename in glob.glob('*.txt'):
     with open(filename, 'r') as f:
         list_of_meetings.append(f.read())
         f.close()
         
len(list_of_meetings) #1236 ^^ THIS WORKED! It's slow, but it worked!
# still contains \n though - will ask about this

# create Series from list 
import pandas as pd
meetingseries = pd.Series(list_of_meetings)

# create DF from Series
meetingframe = meetingseries.to_frame('meeting_text') # create df, name column "meeting_text"

# set index for dataframe merge
meetingframe['id'] = meetingframe.index

# read in working CSV file
# working dir: UN/
recs = pd.read_table('clean_records_copy.csv', sep=',')

# set index for df merge
recs['id'] = recs.index

# Merge on 'id'
full_data = pd.merge(recs, meetingframe)
         
# drop 'id' column
full_data.drop('id', axis=1, inplace=True)

# Write to new CSV file
# full_data.to_csv('full_dataset.csv', index=False, sep = ',') # this gets really screwed up
# how to write clean to CSV?

''' PART 1 - Train Test Split, Naive Bayes, SKLEARN'''

# Train test split
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(full_data.meeting_text, full_data.category, random_state=1)
X_train.shape # 927
X_test.shape # 309

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()
train_dtm = vect.fit_transform(X_train)
test_dtm = vect.transform(X_test)

# Naive Bayes
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(train_dtm, y_train)

y_pred_class = nb.predict(test_dtm)

# Calculate accuracy
from sklearn import metrics
metrics.accuracy_score(y_test, y_pred_class) # 54%

# Print confusion matrix
metrics.confusion_matrix(y_test, y_pred_class)

y_pred_prob = nb.predict_proba(test_dtm)[:, 1]
print y_pred_prob # to check
metrics.roc_auc_score(y_test, y_pred_prob) # AUC score 0.64

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

# false negatives
X_test[y_test > y_pred_class]

''' PART 2 - NTLK '''
# assemble corpus
# save corpus
# load corpus
# train classifier






