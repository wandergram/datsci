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
         