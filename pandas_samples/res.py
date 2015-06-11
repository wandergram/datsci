import pandas as pd

# set column headers
res1_cols = ['id', 'res', 'topic']
# read in csv file of UN Security Council resolutions & topics 
# separate by commas, set names
res1 = pd.read_table('res.csv', sep = ',', names = res1_cols)

# split initial "res" column by " (", assign to new dataframe
year_df = res1['res'].apply(lambda x: pd.Series(x.split(' (')))
# in the new dataframe, create an index column with the
# same name as the index column in the first dataframe
year_df['id'] = year_df.index

# merge the two dataframes - 1) topics & 2) res numbers + years
full_df = pd.merge(res1, year_df)	
# in the column with years, get rid of the closing parentheses	
full_df[1] = full_df[1].map(lambda x: x.lstrip(')').rstrip(')'))

# rename columns
full_df.rename(columns={1:'year', 0:'res'}, inplace=True)
# make years integers
full_df.year = full_df.year.map(lambda x: int(x))

# to be able to sort by them
full_df.groupby('year').count()
# get list of topic counts by year
full_df.groupby(['year', 'topic']).count()
# get list of topics
full_df.groupby('topic').count()

''' Note: earlier ASCII encoding errors were due to
improper reading of special characters.
'''  