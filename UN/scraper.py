# Updated:
# The purpose of this script is to assemble a full sortable CSV file of all meeting records
# and corresponding outcomes (resolutions) by scraping the lists of records/outcomes by year
# off the UN website. This sortable CSV will help determine how many text files will be
# used in the analysis and what topics they cover.

# The files containing text to be analyzed are being downloaded manually. 
# I wrote several catch-all bash scripts to try to automate 
# this process; unfortunately, the UN document system portal restricts access
# to its documents for these types of scripts. 

import sys

reload(sys)
sys.setdefaultencoding('utf8')

# used to handle special Latin characters

import csv
import requests
import pandas as pd

from bs4 import BeautifulSoup

# Step 1.
# Generates csv files of document data for each year

for num in range(1994,2016):
    url = 'http://www.un.org/en/sc/meetings/records/' + str(num) + '.shtml'
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)

    table = soup.find('table', attrs={'class': 'tablefont'})

    list_of_rows = []
    for row in table.findAll('tr'):
        list_of_cells = []
        for cell in row.findAll('td'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)

    outfile = open("./cells" + str(num) + ".csv", "wb")
    writer = csv.writer(outfile)
    writer.writerows(list_of_rows)

# Step 2.
# Concatenates CSV files:

fout = open("record_list.csv","a")
# First file:
for line in open("cells1994.csv"):
    fout.write(line)
    
# Remaining files:    
for num in range(1995,2016):
    f = open("cells"+str(num)+".csv")
    f.next() # skips one header row
    f.next() # skips another header row; each csv file as written from BeautifulSoup had two header rows
    for line in f:
         fout.write(line)
    f.close()
fout.close()

# Step 3. 
# Read in resulting (full) CSV file, add headers:
recs_cols = ['record', 'day', 'press_release', 'topic', 'outcome']
recs = pd.read_table('record_list.csv', sep=',', header=None, names=recs_cols)

# Check CSV file:
recs.head()

# Sort by record number, save sorted order:
recs.sort('record', inplace=True)    

# Write to CSV, sorted:
recs.to_csv('record_list_sorted.csv', index=False)

'''
Tasks to perform:
1. Separate out years from outcomes, add separate column for years (review old code)
2. Examine data via groupby (years, topics)
'''