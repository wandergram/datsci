'''
The code below uses NLTK to see how well it can predict the category of a given 
resolution using a Naive Bayes Classifier. 

This code uses the UNSCR(outcomes) text corpus, not the meeting records (inputs) corpus.
'''
import string
from itertools import chain

from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.classify import NaiveBayesClassifier as nbc
from nltk.corpus import CategorizedPlaintextCorpusReader
import nltk

# working dir: UN/
mydir = 'corpus/unscrs_renamed_categorized'

mr = CategorizedPlaintextCorpusReader(mydir, r'(?!\.).*\.txt', cat_pattern=r'(intervention|soft_action)/.*', encoding='utf-8')
stop = stopwords.words('english')
documents = [([w for w in mr.words(i) if w.lower() not in stop and w.lower() not in string.punctuation], i.split('/')[0]) for i in mr.fileids()]

word_features = FreqDist(chain(*[i for i,j in documents]))
word_features = word_features.keys()[:100]

numtrain = int(len(documents) * 90 / 100)
train_set = [({i:(i in tokens) for i in word_features}, tag) for tokens,tag in documents[:numtrain]]
test_set = [({i:(i in tokens) for i in word_features}, tag) for tokens,tag  in documents[numtrain:]]

classifier = nbc.train(train_set)
print nltk.classify.accuracy(classifier, test_set) # .58 - slightly better!
classifier.show_most_informative_features(20)

'''
Most Informative Features
                  Ivoire = True           interv : soft_a =     18.8 : 1.0
              sustaining = True           interv : soft_a =     13.1 : 1.0
              immunities = True           interv : soft_a =     10.1 : 1.0
                eligible = True           interv : soft_a =      6.6 : 1.0
                arbitral = True           interv : soft_a =      5.2 : 1.0
             electricity = True           interv : soft_a =      4.5 : 1.0
         intensification = True           soft_a : interv =      4.4 : 1.0
                postpone = True           interv : soft_a =      3.7 : 1.0
                granting = True           interv : soft_a =      3.1 : 1.0
               designing = True           soft_a : interv =      2.4 : 1.0
                regional = True           interv : soft_a =      2.1 : 1.0
                     968 = True           soft_a : interv =      2.1 : 1.0
                 Western = True           soft_a : interv =      2.1 : 1.0
                sécurité = True           interv : soft_a =      2.1 : 1.0
                     279 = True           interv : soft_a =      2.1 : 1.0
                   UNODC = True           interv : soft_a =      1.7 : 1.0
                   aegis = True           soft_a : interv =      1.7 : 1.0
                regional = False          soft_a : interv =      1.4 : 1.0
                  second = True           interv : soft_a =      1.4 : 1.0
                    four = True           interv : soft_a =      1.4 : 1.0
'''

