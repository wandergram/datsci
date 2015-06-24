import requests
from bs4 import BeautifulSoup
import pandas as pd
# define a function that accepts an IMDb ID and returns a dictionary of movie information
# There is probably a more elegant way to do this
def get_movie_info(movie_id):
    r = requests.get('http://www.imdb.com/title/tt0111161')
    b = BeautifulSoup(r.text)
    title = b.find(name='span', attrs={'itemprop': 'name', 'class':'itemprop'}).text
    star_rating = b.find(name='div', attrs={'class': 'titlePageSprite star-box-giga-star'}).text
    description = b.find(name='p', attrs={'itemprop':'description'}).text.strip()
    content_rating = b.find(name='meta', attrs={'itemprop':'contentRating'})['content']
    duration = int(b.find(name='time', attrs={'itemprop':'duration'})['datetime'][2:-1])
    return {'title': title, 'star_rating': star_rating, 'description': description, 'content_rating': content_rating, 'duration': duration }    
    
# test the function
get_movie_info('tt0111161')

# open the file of IDs (one ID per row), and store the IDs in a list
with open('imdb_ids.txt', 'r') as f:
    movie_ids = [line.strip() for line in f]

# get the information for each movie, and store the results in a list
movies = [get_movie_info(movie_id) for movie_id in movie_ids]

# check that the list of IDs and list of movies are the same length
assert(len(movies)==len(movie_ids))

# convert the list of movies into a DataFrame
movie_df = pd.DataFrame(movies)
id_df = pd.DataFrame(movie_ids)
