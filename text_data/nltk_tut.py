# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 21:17:11 2015

@author: alex
"""
import nltk
nltk.corpus.gutenberg.fileids()

whit = nltk.corpus.gutenberg.words('whitman-leaves.txt')
len(whit)

from nltk.corpus import gutenberg
gutenberg.fileids()
# returns same as above

whit = gutenberg.words('whitman-leaves.txt')

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    num_sents = len(gutenberg.sents(fileid))
    print int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid

from nltk.corpus import brown
brown.categories()

brown.words(categories='news')

from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will']

for m in modals:
    print m + ':', fdist[m]
    
belles = brown.words(categories='belles_lettres')
fdist2 = nltk.FreqDist([w.lower() for w in belles])

for m in modals:
    print m + ':', fdist2[m]    
    
# obtain counts
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
        
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']

cfd.tabulate(conditions=genres, samples=modals)

# plots with CFD
from nltk.corpus import inaugural
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))

cfd.plot()

# more plots, universal declaration of human rights
# cumulative word length distributions
from nltk.corpus import udhr
languages = ['Chickasaw', 'Greenlandic_Inuktikut', 'Quechua', 'Indonesian', 'French_Francais']
cfd = nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages 
    for word in udhr.words(lang + '-Latin1'))

cfd.plot(cumulative=True)
raw_text = udhr.raw('Javanese-Latin1')
nltk.FreqDist(raw_text).plot()

udhr.fileids()

