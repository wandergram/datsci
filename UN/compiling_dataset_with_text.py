# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 22:05:54 2015

@author: alex
"""

import glob
import sys

# working dir: meeting_records_clean_final
list_of_meetings = []
for filename in glob.glob('*.txt'):
     with open(filename, 'r') as f:
         meetinglist = f.read()
         
         