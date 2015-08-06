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

# clean list
list_of_meetings = [x.replace('\n', ' ') for x in list_of_meetings]
list_of_meetings = [x.replace('_', ' ') for x in list_of_meetings]


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
# full_data.to_csv('full_dataset.csv', index=False)


''' PART 1 - Train Test Split, Naive Bayes, SKLEARN'''

# Train test split
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(full_data.meeting_text, full_data.category, random_state=1)
X_train.shape # 927
X_test.shape # 309

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer() # ngram = 1
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

''' PART 2 '''

#CountVectorizer with ngrams
vect2 = CountVectorizer(ngram_range=(1,5), stop_words = 'english', min_df=2)
train_dtm_n = vect2.fit_transform(X_train)
test_dtm_n = vect2.transform(X_test)

nb = MultinomialNB()
nb.fit(train_dtm_n, y_train)

y_pred_class_n = nb.predict(test_dtm_n)

# Calculate accuracy
metrics.accuracy_score(y_test, y_pred_class_n) 

# 57% for ngram_range 1,2
# 66% with ngram_range 2,3 
# 69% with ngram_range 2,5
# 74% with ngram_range 2,5, stopwords included
# 70% with ngram_range 1,5, stopwords included

print vect2.get_feature_names()[-50:]

''' Logistic Regression '''
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=1e9)
logreg.fit(train_dtm_n, y_train)
y_pred_class = logreg.predict(test_dtm_n)
print metrics.accuracy_score(y_test, y_pred_class_n) # 70%

''' from sklearn tutorial '''
'''
X_train_counts = vect.fit_transform(X_train)
X_train_counts.shape

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape

clf = MultinomialNB().fit(X_train_tfidf, y_train)

new_words = ['acts of genocide', 'atrocities committed by']
X_new_counts = vect.transform(new_words)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for word, category in zip(new_words, predicted):
    print('%r => %s' % (word, y_pred_class_n))

# clf.predict('acts of genocide')

'''








