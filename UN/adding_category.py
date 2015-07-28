# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:05:54 2015

@author: alex
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')
# used to handle special Latin characters

import pandas as pd
import numpy as np
 
# Read in the previously assembled CSV file, add headers to the dataframe:
recs_cols = ['record', 'day', 'press_release', 'topic', 'outcome']
recs = pd.read_table('final_clean_records.csv', sep=',')

# Check dataframe
recs.head()

# Import glob for future use
import glob

# Create category column, fill with NaN values
recs['category'] = np.nan

# Check dataframe with new category column
recs.head()

# Clean previously assembled dataframe from CSV file to tidy up the values in the outcome column
# by splitting the column on the opening parenthesis, cutting off everything after the document number.
# These values previously included the resolution number, the year in parentheses, and sometimes 
# additional values following those.
# Create new dataframe based on clean outcome column.
resolution_df = recs['outcome'].apply(lambda x: pd.Series(str(x).split(' (')))

# Check to make sure this worked
resolution_df.head()

# Drop unnecessary columns created through the split
resolution_df.drop(1, axis=1, inplace=True)
resolution_df.drop(2, axis=1, inplace=True)
resolution_df.drop(3, axis=1, inplace=True)

# Check dataframe again
resolution_df.head()

# Set index for initial dataframe
recs['id'] = recs.index

# Set index for new dataframe with the clean outcome column
resolution_df['id'] = resolution_df.index

# Merge on 'id'
full_clean_records = pd.merge(recs, resolution_df)

# Drop old (dirty) outcome column, drop id column
full_clean_records.drop('outcome', axis=1, inplace=True)
full_clean_records.drop('id', axis=1, inplace=True)

# Rename new (clean) outcome column "outcome"
full_clean_records.rename(columns={0: 'outcome'}, inplace = True)

# Write to new CSV file
full_clean_records.to_csv('final_clean_records_new.csv', index=False)

# Read in new CSV file
newrecords_cols = ['record', 'day', 'press_release', 'topic', 'year', 'category', 'outcome']
newrecords = pd.read_table('final_clean_records_new.csv', sep=',')

# Begin filling in "category" column with 0 for resolutions that fall under soft actions 
# and 1 for resolutions that fall under interventions.
# The glob module here reads the files, finds the corresponding document number,
# matches it against the value of the outcome column, and sets the value in the category column
# to 0 or 1.

for filename in glob.glob('corpus/unscrs_renamed_categorized/soft_action/*.txt'):
    with open(filename, 'r') as f:
        for line in f:
            newrecords[newrecords['outcome'] == line]['category'] = 0
            
for filename in glob.glob('corpus/unscrs_renamed_categorized/intervention/*.txt'):
    with open(filename, 'r') as f:
        for line in f:
            newrecords[newrecords['outcome'] == line]['category'] = 1







