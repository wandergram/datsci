''' With the help of scraper.py, I created a full list of UN Security Council 
records in CSV format and sorted it chronologically. The list includes the reference
number for all records of Security Council meetings, the day and month each meeting was held,
the reference number for the corresponding press release/communique, the topic of 
the meeting, and the reference number for an outcome (a Security Council Resolution - 
SCR - or a Presidential Statement - PRST) if one exists. 

For the purposes of this project, I'm only interested in Security Council Resolutions 
as outcomes, not Presidential Statements. 

The goal was to create a reference list of records that can be explored to inform further 
analysis - I wanted to see the distribution of resolutions and topics across years. 

The CSV list I had scraped and assembled contained only days and months, not years, 
because it had been scraped from individual pages of records for each year (1994 - 2015). 
Information on the year to which a record pertains is contained in the reference number for 
each Security Council Resolution, which follows the format S/RES/XXX (YEAR). Reference numbers 
for Presidential Statements, on the other hand, follow a different format - S/PRST/XXXX. 
I'm only interested in Resolutions, not Statements, so this differentiation is very handy -
I can extract the year from each Resolution reference number, add the years to a new column,
replace the reference numbers for Presidential Statements with NaN, and remove those observations
where the outcome was anything other than a Resolution.  

The code below reads this CSV file into a dataframe, adds a year column for each record by parsing
the reference number for each outcome and determining whether it's a Resolution or a Statement,
cleans the data so that the only observations that remain are those I'm interested in,
and writes the result out to a new CSV file.  
'''

import sys

reload(sys)
sys.setdefaultencoding('utf8')
# used to handle special Latin characters

import csv
import pandas as pd
 
# Read in the starting CSV file, add headers to the dataframe:
recs_cols = ['record', 'day', 'press_release', 'topic', 'outcome']
recs = pd.read_table('record_list_sorted_copy.csv', sep=',')

# Check dataframe:
recs.head()  

# Parse the outcome column, split it by the opening parenthesis that contains the year.
# This will affect only outcomes that are Resolutions, following the format S/RES/XXX (YEAR).
# If there's no parenthesis, it's a Presidential Statement, and I don't need it.
# Write the results to a new dataframe.
year_df = recs['outcome'].apply(lambda x: pd.Series(str(x).split(' (')))

# In the first series of the new dataframe, slice everything before the year.
year_df[0] = year_df[0].map(lambda x: str(x)[:-17])

# Create a new dataframe, this time splitting the series by the closing parenthesis.
year_df_2 = year_df[1].apply(lambda x: pd.Series(str(x).split(')')))

# In the new dataframe, drop the columns I don't need that were created during the steps above.
year_df_2.drop(1, axis=1, inplace = True)  

# Set an index for the starting dataframe.
recs['id'] = recs.index

# Set index for the clean dataframe of years.
year_df_2['id'] = year_df_2.index

# Merge the two on 'id' into a new dataframe.
full_records = pd.merge(recs, year_df_2)

# Drop the 'id' column of the new dataframe.
full_records.drop('id', axis = 1, inplace = True)

# Check the resulting shape. We have 4,391 rcords.
full_records.shape
# 4391 observations

# In the new dataframe, rename the year column.
full_records.rename(columns={0: 'year'}, inplace = True)

# Remove all observations with the value 'nan' for year. Those aren't Resolutions, they're 
# Presidential Statements.
full_records = full_records[full_records.year != 'nan']

# Check shape again - 1,304 observations. 
full_records.shape

# Write to CSV:
full_records.to_csv('clean_records_with_years.csv', index=False)

# Groupbys:
full_records.groupby('year').count()
# something's off with data here, review
