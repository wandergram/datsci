# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:19:21 2015

@author: alex
"""

''' Read file, if it contains a certain string, rename it '''

# testing finding lines
for line in open("2014-N1469720.txt"):
 if "United Nations" in line:
   print line
   
# testing opening files in folder
# this was a surprisingly quick process given the amount of lines to print!
import glob
for filename in glob.glob('*.txt'):
    for line in open(filename):
        if "United Nations" in line:
            print line
        
# testing other commands
# chapter VII missions
list_of_ch7 = []
import glob
for filename in glob.glob('*.txt'):
    for line in open(filename):
        if "under Chapter VII" in line:
            print filename
            list_of_ch7.append(filename)
            
print list_of_ch7

# embargoes
embargoes = []
for filename in glob.glob('*.txt'):
    for line in open(filename):
        if "States shall prevent" in line:
            print filename
            embargoes.append(filename)
            
print embargoes

# all necessary means
all_means = []
for filename in glob.glob('*.txt'):
    for line in open(filename):
        if "use all necessary means" in line:
            print filename
            all_means.append(filename)
            
print all_means

# observers
observers = []
for filename in glob.glob('*.txt'):
    for line in open(filename):
        if "United Nations observers" in line:
            print filename
            observers.append(filename)
            
print observers

# other deployments
deploy = []
for filename in glob.glob('*.txt'):
    for line in open(filename):
        if "identify personnel, plan and make" in line:
            print filename
            deploy.append(filename)
            
print deploy
            
# define a single function for this
# find expression in file, append to list
            
def find_files(lists, expressions):
    for filename in glob.glob('*.txt'):
        for line in open(filename):
            if expressions in line:
                print filename
                lists.append(filename)
    print lists
    
# run function 
# extension of mission
mission_extend = []
find_files(mission_extend, "extend the present mandate")
find_files(mission_extend, "extend the mandate")
find_files(mission_extend, "renew the mandate")

len(mission_extend) # 502
len(set(mission_extend)) # 480 - includes duplicates, should deal with this later

# drawdown of mission
drawdown = []
find_files(drawdown, "drawdown")
len(drawdown)
find_files(drawdown, "gradual reduction of")
len(drawdown)
len(set(drawdown))

# define a function to explore the text to validate logic
def explore(strings):
    for filename in glob.glob('*.txt'):
        for line in open(filename):
            if strings in line:
                print line

explore("States shall prevent")

explore("economic activities")

# sanctions
sanctions = []
find_files(sanctions, "economic activities carried on, after the date of adoption of this")
   
# define rules for renaming
# define bin numbers
soft = "11"
prohib = "22"
hard = "33"
extend = "44"
hard_neg = "55" # mission drawdown
prohib_neg = "66" # sanctions cancellation
soft_neg = "77" # observer handover

# everything else will be read as "no action"

# copied all UNSCRs in working dir to other dir in case this blows up!

# renaming the resolutions that deal with mission extensions
import os
for filename in os.listdir("."):
    if filename in mission_extend:
        os.rename(filename, extend+filename)
        print filename

# defining function to rename files by previously assembled list
def rename_files(list_name, var_name):
    for filename in os.listdir("."):
        if filename in list_name:
            os.rename(filename, var_name+filename)
            print filename

# rename files referencing hard measures
rename_files(list_of_ch7, hard)

# rename files referencing mission drawdown
rename_files(drawdown, hard_neg)

# rename files referencing embargoes
rename_files(embargoes, prohib)

# explore travel ban-related resolutions
explore("prevent the entry into or transit through their territories")  
# create travel ban list
travel_ban = []
find_files(travel_ban, "prevent the entry into or transit through their territories") 

# rename files
rename_files(travel_ban, prohib)