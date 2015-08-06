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

# many more false positives, very few false negatives
# high sensitivity, low specificity

''' PART 2 '''

#CountVectorizer with ngrams
vect2 = CountVectorizer(ngram_range=(5,5), stop_words = 'english', min_df=2)
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
# 75% with ngram_range 5,5, stopwords included

nb.predict(test_dtm_n[72]) # this alone won't access the feature.
# only the ordinal in the numpy array

print vect2.get_feature_names()[-50:]

# Got this code off of Stack Overflow
# http://stackoverflow.com/questions/11116697/how-to-get-most-informative-features-for-scikit-learn-classifiers
# Used to get most informative features for linear models in scikit-learn
def show_most_informative_features(vect2, nb, n=20):
    feature_names = vect2.get_feature_names()
    coefs_with_fns = sorted(zip(nb.coef_[0], feature_names))
    top = zip(coefs_with_fns[:n], coefs_with_fns[:-(n + 1):-1])
    for (coef_1, fn_1), (coef_2, fn_2) in top:
        print "\t%.4f\t%-15s\t\t%.4f\t%-15s" % (coef_1, fn_1, coef_2, fn_2)
        
print show_most_informative_features(vect2, nb)

'''
        -11.9945        000 people lost lives endless           -5.1121 kingdom great britain northern ireland
        -11.9945        04 2014 meeting called order            -5.1141 united kingdom great britain northern
        -11.9945        07 2014 meeting called order            -5.6974 great britain northern ireland united
        -11.9945        07 2014 president floor representative          -5.8568 northern ireland united states america
        -11.9945        10 20 meeting called order              -5.8568 britain northern ireland united states
        -11.9945        10 20 new york president                -6.0258 sent signature member delegation concerned
        -11.9945        10 2013 meeting called order            -6.0284 security council corrections submitted original
        -11.9945        10 despite present quiet israeli                -6.0284 records security council corrections submitted
        -11.9945        10 president like inform council                -6.0309 text printed official records security
        -11.9945        10 year capacity building plan          -6.0309 printed official records security council
        -11.9945        10 years security council äôs           -6.0309 official records security council corrections
        -11.9945        1044 1996 send clear unambiguous                -6.0309 languages final text printed official
        -11.9945        1062 contains text draft resolution             -6.0309 final text printed official records
        -11.9945        1063 contains text draft resolution             -6.0439 record sent signature member delegation
        -11.9945        11 15 new york president                -6.0439 incorporated copy record sent signature
        -11.9945        11 25 adoption agenda agenda            -6.0439 copy record sent signature member
        -11.9945        11 25 new york president                -6.0465 speeches delivered languages final text
        -11.9945        11 35 new york president                -6.0465 delivered languages final text printed
        -11.9945        11 50 new york president                -6.0623 security council concluded present stage
        -11.9945        11 april 1996 charg äôaffaires          -6.0676 present stage consideration item agenda
'''

# Other option, also from Stack Overflow
# Run with Class 0 first (soft action)
def most_informative_feature_for_class(vectorizer, classifier,  n=10):
    labelid = list(classifier.classes_).index(0)
    feature_names = vectorizer.get_feature_names()
    topn = sorted(zip(classifier.coef_[labelid], feature_names))[-n:]

    for coef, feat in topn:
        print feat, coef

print most_informative_feature_for_class(vect2, nb)

'''
printed official records security council -6.03094476782
text printed official records security -6.03094476782
records security council corrections submitted -6.02837737231
security council corrections submitted original -6.02837737231
sent signature member delegation concerned -6.02581655145
britain northern ireland united states -5.85679705735
northern ireland united states america -5.85679705735
great britain northern ireland united -5.6974147915
united kingdom great britain northern -5.11414002925
kingdom great britain northern ireland -5.11208664044
'''

# Run with Class 1
''' this produces an error
def most_informative_feature_for_class(vectorizer, classifier,  n=10):
    feature_names = vectorizer.get_feature_names()
    topn = sorted(zip(classifier.coef_[1], feature_names))[-n:]

    for coef, feat in topn:
        print feat, coef
        
print most_informative_feature_for_class(vect2, nb)
'''

''' Logistic Regression '''

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=1e9)
logreg.fit(train_dtm_n, y_train)
y_pred_class = logreg.predict(test_dtm_n)
print metrics.accuracy_score(y_test, y_pred_class_n) # 70%










