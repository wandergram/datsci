# Here I add another column to the dataset to set the year
# for each observation. 

import sys

reload(sys)
sys.setdefaultencoding('utf8')
# used to handle special Latin characters

import csv
import pandas as pd
 
# Read in full CSV file, add headers:
recs_cols = ['record', 'day', 'press_release', 'topic', 'outcome']
recs = pd.read_table('record_list_sorted_2.csv', sep=',')

# Check dataframe:
recs.head()  

# strip 
year_df = recs['outcome'].apply(lambda x: pd.Series(str(x).split(' (')))

# strip again
year_df[0] = year_df[0].map(lambda x: str(x)[:-17])

# strip again
year_df_2 = year_df[1].apply(lambda x: pd.Series(str(x).split(')')))

# drop 1
year_df_2.drop(1, axis=1, inplace = True)  

# set index for recs
recs['id'] = recs.index

# set index for years
year_df_2['id'] = year_df_2.index

# merge
full_records = pd.merge(recs, year_df_2)

# drop id
full_records.drop('id', axis = 1, inplace = True)

# check shape
full_records.shape
# 4391 observations

# rename 0 column to year
full_records.rename(columns={0: 'year'}, inplace = True)

# remove observations with nan for year, those aren't resolutions
full_records = full_records[full_records.year != 'nan']

# check shape again - 1304 observations

# Write to CSV, sorted:
full_records.to_csv('clean_records_with_years.csv', index=False)

# Groupbys
full_records.groupby('year').count()
# something's off with data here, review