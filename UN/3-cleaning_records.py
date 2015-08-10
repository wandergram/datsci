''' After scraping records and adding years, I ran some groupby operations
and noticed that there were reference numbers in the "year" column that 
were in a different format (not S/RES/XXX (YEAR)) and didn't get converted to 
years during the data cleaning process. This means that these were reference 
numbers for other types of documents - notes, communiques, etc - and not 
resolutions, so I can safely discard these records and write a new CSV file. 
'''

import sys

reload(sys)
sys.setdefaultencoding('utf8')
# used to handle special Latin characters

import csv
import pandas as pd
 
# Read in the starting CSV file, add headers to the dataframe:
clean_recs_cols = ['record', 'day', 'press_release', 'topic', 'outcome', 'year']
clean_records = pd.read_table('clean_records_with_years.csv', sep=',')

# Check dataframe:
clean_records.head()  

# Check shape
clean_records.shape
# 1,304 records

# Check groupby:
clean_records.groupby('year').count()

'''
Found a few instances of dirty data here - values in the year column that
are reference numbers for records following a different format, not years (e.g. 
S/1994/1176 instead of 1994). Because they followed a different format, not 
S/RES/XXX (YEAR), they weren't affected by the split functions applied previously. 

Looking through the data, these are records for observations in which the outcomes
were notes, drafts, communiques, or vetoed resolutions - in other words,
outcomes that aren't relevant to this project. I'll get rid of them below.
'''

# Remove all rows in which the value for "year" is anything other than a 4-digit year
clean_records = clean_records[clean_records['year'].map(len) == 4]

# Check shape again - 1,283 observations. 
clean_records.shape

# New groupbys:
clean_records.groupby('year').count()
# Verified that we've left only relevant records.

clean_records.groupby('year').topic.describe().head(50)
clean_records.groupby('year').topic.describe().tail(50)
'''
Starting to get a better idea of topic distribution by year.
Most popular topics: 
1994 - Rwanda, 
1995 - Bosnia, 
1996 - Croatia, 
1997-1998 - Angola, 
1999 - Western Sahara,
2000 - Sierra Leone,
2001-2002 - Afghanistan,
2003-2004 - DR Congo,
2005 - Cote d'Ivoire,
2006 - Middle East,
2007 - DR Congo,
2008 - Somalia,
2009 - Middle East,
2010 - Cote d'Ivoire,
2011 - Cote d'Ivoire,
2012 - Middle East,
2013 - Somalia,
2014 - Middle East,
2015 - Sudan.
'''
# Write to CSV:
clean_records.to_csv('final_clean_records.csv', index=False)
