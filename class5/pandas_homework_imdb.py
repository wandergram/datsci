'''
Pandas Homework with IMDB data
'''

'''
BASIC LEVEL
'''

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
# imported to get rid of ascii encoding errors in movie names with special chars

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
movies = pd.read_table('imdb_1000.csv', sep=',')

# check the number of rows and columns
movies.shape

# check the data type of each column
movies.dtypes

# calculate the average movie duration
movies.duration.mean()

# sort the DataFrame by duration to find the shortest and longest movies
movies.sort('duration', ascending=False).head(10)
movies.sort('duration', ascending=False).tail(10)
# same as movies.sort('duration').head(10)

# create a histogram of duration, choosing an "appropriate" number of bins
movies.duration.plot(kind='hist', bins=np.arange(50,250), color='#7D2AAD')
plt.xlabel("Duration, minutes")
plt.ylabel("Number of movies")
# ^^ let numpy define range for bins between shortest and longest movie;
# this worked better visually than setting bins to 25 or 30, because
# we can clearly see a spike at around 120 minutes. However, setting bins to 
# 25 let us see more observations in larger chunks, with the y-axis labeled
# in 20-ct increments from 0 to 140.

# use a box plot to display that same data
movies.duration.plot(kind='box', color="k")

'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
movies.content_rating.value_counts()

# use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind='bar', title='Number of movies per content rating category')
plt.xlabel('Ratings')
plt.ylabel('Movies')

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
movies.content_rating.replace('NOT RATED', 'UNRATED', inplace=True)
movies.content_rating.replace('APPROVED', 'UNRATED', inplace=True)
movies.content_rating.replace('PASSED', 'UNRATED', inplace=True)
movies.content_rating.replace('GP', 'UNRATED', inplace=True)

# convert the following content ratings to "NC-17": X, TV-MA
movies.content_rating.replace('X', 'NC-17', inplace=True)
movies.content_rating.replace('TV-MA', 'NC-17', inplace=True)

# count the number of missing values in each column
movies.isnull().sum()

# if there are missing values: examine them, then fill them in with "reasonable" values
movies.content_rating.fillna(value='UNRATED', inplace=True)

# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours
movies[movies.duration >= 120 ].star_rating.mean() # ~7.95
movies[movies.duration < 120].star_rating.mean() # ~7.84

# use a visualization to detect whether there is a relationship between star rating and duration
movies.plot(kind='scatter', x='duration', y='star_rating', alpha=0.3, color='#0066cc')
'''
Most movies appear to fall around the two-hour mark in duration and are rated
between 7.5-8.5. 
'''

# calculate the average duration for each genre
movies.groupby('genre').duration.mean()

'''
Longest/shortest movie:
'''

movies[movies.duration == movies.duration.min()][['title', 'star_rating', 'duration', 'genre']]

movies[movies.duration == movies.duration.max()][['title', 'star_rating', 'duration', 'genre']]

# same can be done for ratings

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration
movies.boxplot(column='duration', by='content_rating')
''' 
Observations:
Lots of outliers among R-rated movies;
On average, PG-13-rated movies are longer than movies with other ratings;
G-rated movies are the shortest, as expected (cartoons, childrens' movies);
Widest range of durations among unrated movies, also as expected (indie films, etc);
'''

# determine the top rated movie (by star rating) for each genre

# Attempt 1 - the code below gets us 50% of the way there, listing ratings for
# each movie in each genre in ascending order. Sort doesn't work, 
# says bool object is not callable.
movie_ratings = movies.groupby(['genre', 'star_rating']).title.agg('max')

# Attempt 2 - because the index has no duplicate values,
# idxmax lets us select the index of row with the max star_rating
# for each group of genres. Then, loc lets us select the row. 
movies.loc[movies.groupby('genre').star_rating.agg('idxmax')]

# However, the result is clunky and difficult to read. 
# So we use drop to get rid of the extra columns and simplify the code a bit:
top_ratings = movies.loc[movies.groupby('genre').star_rating.agg('idxmax')]
top_ratings.drop(['content_rating', 'duration', 'actors_list'], axis=1) 

# check if there are multiple movies with the same title, and if so, determine if they are the same movie
movies.set_index('title').index.get_duplicates()
movies[movies.title.duplicated()] # same as above
movies.duplicated(['title']).sum() # total 4, as above
# unsure why these are considered duplicates? 

# calculate the average star rating for each genre, but only include genres with at least 10 movies
# 1 - understand data
movies.genre.describe()

# 2 group by star rating
movies.groupby('genre').star_rating.mean() 

# 3 - select genres with at least 10 movies by boolean indexing
atleast_10 = movies.groupby('genre').title.count() >= 10

# 4 - create series
movie_genres = movies.groupby('genre').agg({'star_rating': ['mean']})

# 5 - apply atleast_10 to sort 
movie_genres[atleast_10].sort([('star_rating', 'mean')], ascending=False)


'''
BONUS
'''

# Figure out something "interesting" using the actors data!
