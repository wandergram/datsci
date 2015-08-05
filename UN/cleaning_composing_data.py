# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:36:04 2015

@author: alex
"""
'''
The purpose of this code was to determine why I had 1236 meeting records in my working CSV file
and only 1229 files in my meeting records corpus.
There is likely a way to refactor this more elegantly; however, going back and forth
from pandas objects to lists was fairly easy.
I also discovered some errors in the way new, clean(er) copies of the CSV file were written;
a lot of these issues turned out to be much easier to find and remedy by hand in Excel.
'''
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import pandas as pd
import glob

# working dir: meeting_records_clean
list_of_pvs = []
for filename in glob.glob('*.txt'):
    list_of_pvs.append(filename)

''' lost a bunch of code here; thankfully wrote to new CSV beforehand.
Note: Spyder keeps crashing, this is a known OS X bug.
'''

len(list_of_pvs) #1229

# create clean df from list of filenames

listpvs = pd.Series(list_of_pvs)
listframe = listpvs.to_frame('recnum') # here I write to a df and set "recnum" as the column name

listdf1 = listframe['recnum'].apply(lambda x: pd.Series(str(x).split('-'))) # drops year from front of filename
listdf1.drop(0, axis=1, inplace = True)
listdf2 = listdf1[1].apply(lambda x: pd.Series(str(x).split('.'))) # drops .txt from end of filename
listdf2.drop(1, axis=1, inplace = True)

listdf2.rename(columns={0: 'recnum'}, inplace = True)

# read in records from working CSV file

recs = pd.read_table('clean_records_copy.csv', sep=',')

# clean "record_number" column from working CSV file
recdf = recs['record_number'].apply(lambda x: pd.Series(str(x).split('+')))

# clean again

recdf2 = recdf[0].apply(lambda x: pd.Series(str(x).split(' (')))
recdf2.drop(1, axis=1, inplace = True)

# create list from filename df
filename_list = listdf2['recnum'].tolist() # length is 1229

# create list from record number df
record_list = recdf2[0].tolist() # length is 1236

# figure out where the difference is!
list_diff = [x for x in record_list if x not in filename_list]

'''
['3698(Resumption 2)',
 '4844',
 '4849',
 '4850',
 '5040',
 '5048',
 '5082(meeting held in Nairobi)',
 '5726',
 '5868  ',
 '5916  ']
 

'''

# found six files that were definitively missing from records
# these files were downloaded, converted and added to the corpus
# also established that the CSV file has two entries with identical meeting record numbers
# that generated two distinct resolutions, which is where the discrepancy lies.
# To resolve this difference, I copied the file with the meeting record under the duplicate number and
# assigned it a different number. This shouldn't affect the model because 
# the same meeting led to two different resolutions.
# Confirmed that no other data is missing. 