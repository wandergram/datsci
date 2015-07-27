# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 20:20:40 2015

@author: alex
"""
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'Desktop/datsci/UN/corpus/meeting_records/'
pvs = PlaintextCorpusReader(corpus_root, '.*', encoding='utf8')
pvs.fileids()

''' note: setting the encoding in two different places wouldn't fix the 
problem of latin-1 characters and unicode encoding. 
I tried a few different bash scripts, but none worked and I nearly overwrote 
all of my files (a good reminder to make 67 backups).
For Mac OSX, I used an app called TEConverter to batch convert to UTF-8. 
'''
# plots conditional frequency distributions of words across years

# genocide, atrocities, massacres, cleansing
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4]) # separates the years out of the filenames for the X axis
    for fileid in pvs.fileids()
    for w in pvs.words(fileid)
    for target in ['genocid', 'atrocit', 'massacre', 'cleansing'] 
    if w.lower().startswith(target))

cfd.plot()

# demands
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4]) # separates the years out of the filenames for the X axis
    for fileid in pvs.fileids()
    for w in pvs.words(fileid)
    for target in ['demand'] 
    if w.lower().startswith(target))

cfd.plot()