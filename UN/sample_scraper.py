# Working on a script that would loop through all years btween 1994-2015.
# The purpose of this script is just to assemble a CSV file of all meeting records
# and corresponding outcomes (resolutions). The files containing text to be analyzed
# are being downloaded manually. I wrote several catch-all bash scripts to try to automate 
# this process; unfortunately, the UN document system portal restricts access
# to its documents for these types of scripts. 

import sys

reload(sys)
sys.setdefaultencoding('utf8')

# used to handle special Latin characters

import csv
import requests

from bs4 import BeautifulSoup

url = 'http://www.un.org/en/sc/meetings/records/2015.shtml'
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

outfile = open("./cells15.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
