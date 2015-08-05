# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:13:44 2015

@author: alex
"""
import glob
import pandas as pd
# working dir: corpus/meeting_records_clean_final/
# create list of filenames
list_of_pvs = []
for filename in glob.glob('*.txt'):
    list_of_pvs.append(filename)

# working dir: UN
# create list of category values
recs = pd.read_table('clean_records_copy.csv', sep=',')

category_list = recs['category'].tolist()

# create dictionary from two lists
# includes filename, category from CSV file
keys = list_of_pvs
values = category_list
dictionary = dict(zip(keys, values))

# using the created dictionary, put files into one of two folders
import shutil
import os
source = r"/Users/alex/Desktop/datsci/UN/corpus/meeting_records_clean_final"
destination = r"/Users/alex/Desktop/datsci/UN/corpus/meeting_records_final_categorized"

def move_files(destination, cat):
    if not os.path.exists(destination):
        os.makedirs(destination) 
    for f in os.listdir(source):             
        for key, value in dictionary.iteritems():
            if key == f:
                if value == int(cat): 
                    shutil.move(os.path.join(source,f), destination)

# Move all files whose category is 0 to a folder called "soft_action"
move_files(r"/Users/alex/Desktop/datsci/UN/corpus/meeting_records_final_categorized/soft_action", "0")

# Move all files whose category is 1 to a folder called "intervention"
move_files(r"/Users/alex/Desktop/datsci/UN/corpus/meeting_records_final_categorized/intervention", "1")


'''
The code below uses NLTK to see how well it can predict the category of a given 
resolution using a Naive Bayes Classifier. 

This code uses the meeting records (inputs) corpus.
'''
import string
from itertools import chain

from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.classify import NaiveBayesClassifier as nbc
from nltk.corpus import CategorizedPlaintextCorpusReader
import nltk

# working dir: UN/
mydir = 'corpus/meeting_records_final_categorized'

mr = CategorizedPlaintextCorpusReader(mydir, r'(?!\.).*\.txt', cat_pattern=r'(intervention|soft_action)/.*', encoding='utf-8')
stop = stopwords.words('english')
documents = [([w for w in mr.words(i) if w.lower() not in stop and w.lower() not in string.punctuation], i.split('/')[0]) for i in mr.fileids()]

word_features = FreqDist(chain(*[i for i,j in documents]))
word_features = word_features.keys()[:100]

numtrain = int(len(documents) * 90 / 100)
train_set = [({i:(i in tokens) for i in word_features}, tag) for tokens,tag in documents[:numtrain]]
test_set = [({i:(i in tokens) for i in word_features}, tag) for tokens,tag  in documents[numtrain:]]

classifier = nbc.train(train_set)
print nltk.classify.accuracy(classifier, test_set) # .87 - ?!?!?!
classifier.show_most_informative_features(20)

'''
Most Informative Features
              immunities = True           interv : soft_a =      4.4 : 1.0
               designing = True           soft_a : interv =      4.2 : 1.0
                 Western = True           soft_a : interv =      3.5 : 1.0
                   Croat = True           interv : soft_a =      3.2 : 1.0
                  Larsen = True           soft_a : interv =      3.1 : 1.0
                     273 = True           interv : soft_a =      2.8 : 1.0
              affiliated = True           interv : soft_a =      2.5 : 1.0
                 hanging = True           soft_a : interv =      2.5 : 1.0
               localized = True           soft_a : interv =      2.5 : 1.0
             distortions = True           soft_a : interv =      2.5 : 1.0
              sustaining = True           soft_a : interv =      2.2 : 1.0
               Initially = True           interv : soft_a =      2.0 : 1.0
                   Pronk = True           interv : soft_a =      2.0 : 1.0
                  shocks = True           interv : soft_a =      2.0 : 1.0
              regularize = True           interv : soft_a =      2.0 : 1.0
           steadfastness = True           soft_a : interv =      1.9 : 1.0
                   UNITA = True           soft_a : interv =      1.9 : 1.0
                  ÄúWith = True           interv : soft_a =      1.7 : 1.0
                   rebel = True           interv : soft_a =      1.6 : 1.0
                 succumb = True           soft_a : interv =      1.5 : 1.0
'''


