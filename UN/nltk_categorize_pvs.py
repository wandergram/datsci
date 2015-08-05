# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:13:44 2015

@author: alex
"""
import glob
import pandas as pd
# working dir: corpus/meeting_records_clean_final/
# create list of filenames
list_of_pvs = []
for filename in glob.glob('*.txt'):
    list_of_pvs.append(filename)

# working dir: UN
# create list of category values
recs = pd.read_table('clean_records_copy.csv', sep=',')

category_list = recs['category'].tolist()

# create dictionary from two lists
# includes filename, category from CSV file
keys = list_of_pvs
values = category_list
dictionary = dict(zip(keys, values))

# using the created dictionary, put files into one of two folders
import shutil
import os
source = r"/Users/alex/Desktop/datsci/UN/corpus/meeting_records_clean_final"
destination = r"/Users/alex/Desktop/datsci/UN/corpus/meeting_records_final_categorized"

def move_files(destination, cat):
    if not os.path.exists(destination):
        os.makedirs(destination) 
    for f in os.listdir(source):             
        for key, value in dictionary.iteritems():
            if key == f:
                if value == int(cat): 
                    shutil.move(os.path.join(source,f), destination)

# Move all files whose category is 0 to a folder called "soft_action"
move_files(r"/Users/alex/Desktop/datsci/UN/corpus/meeting_records_final_categorized/soft_action", "0")

# Move all files whose category is 1 to a folder called "intervention"
move_files(r"/Users/alex/Desktop/datsci/UN/corpus/meeting_records_final_categorized/intervention", "1")




