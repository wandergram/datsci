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
find_files(mission_extend, "extend its mandate")
find_files(mission_extend, "adjust the mandate")
find_files(mission_extend, "Decides to extend U")
find_files(mission_extend, "Decides to extend M")
find_files(mission_extend, "Decides to extend until")
find_files(mission_extend, "Decides to extend the current mandate")
find_files(mission_extend, "Extends the stationing")
find_files(mission_extend, "to renew the mandate")
find_files(mission_extend, "Decides to renew for a period of")
find_files(mission_extend, "Decides to extend the existing mandate")
find_files(mission_extend, "Authorizes the expansion of M")
find_files(mission_extend, "Approves the expansion of M")
find_files(mission_extend, "Decides to extend")
find_files(mission_extend, "Decides to renew the mandates")
find_files(mission_extend, "increase the overall force levels")

len(mission_extend) # 502
len(set(mission_extend)) # 480 - includes duplicates, should deal with this later

# drawdown of mission
drawdown = []
find_files(drawdown, "drawdown")
len(drawdown)
find_files(drawdown, "gradual reduction of")
find_files(drawdown, "Decides to withdraw U")
find_files(drawdown, "liquidation")
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
find_files(list_of_ch7, "Chapter VII of the Charter")
rename_files(list_of_ch7, hard)

# rename files referencing mission drawdown
rename_files(drawdown, hard_neg)

# rename files referencing embargoes
rename_files(embargoes, prohib)
find_files(embargoes, "the measures on arms")
rename_files(embargoes, prohib)

# explore travel ban-related resolutions
explore("prevent the entry into or transit through their territories")  

# create travel ban list, rename files
travel_ban = []
find_files(travel_ban, "prevent the entry into or transit through their territories") 
rename_files(travel_ban, prohib)

# soft measures - police presence
explore("civilian police")
civilian_police = []
find_files(civilian_police, "civilian police")
rename_files(civilian_police, soft)

# soft measures - military observers
explore("military observers")
military_observ = []
find_files(military_observ, "military observers")
rename_files(military_observ, soft)

# suspension of measures - this doesn't quite work, find other text
# explore("shall be suspended")
# suspend_sanctions = []
# find_files(suspend_sanctions, "shall be suspended")
# rename_files(suspend_sanctions, prohib_neg)

# what else is out there
explore("Decides to")
explore("Decides to terminate")

# suspension of prohibitive measures - review this
suspend_prohib = []
find_files(suspend_prohib, "Decides to terminate the prohibitions")
find_files(suspend_prohib, "Decides to terminate the remaining prohibitions")
rename_files(suspend_prohib, prohib_neg)

# explore("Decides to renew for a period of")

explore("liquidation")
explore("Approves the expansion of M")
explore("Authorizes the expansion of M")
explore("Panel of Experts")

# soft measures - experts
experts = []
find_files(experts, "Panel of Experts")
rename_files(experts, soft)

# what other decisions has it made
explore("1. Decides to")
explore("increase the overall force levels")
explore("advance team")

# soft measures - advance teams (observers, setup)
advance_team = []
find_files(advance_team, "advance team")
rename_files(advance_team, soft)

