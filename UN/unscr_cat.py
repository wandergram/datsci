# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:54:50 2015

@author: alex
"""

''' A clean version of the script to 1) explore the text of UN Security Council 
resolutions (SCRs) (outputs), 2) find files of interest, 3) determine how to categorize them, and 
4) rename the files by category in order to 5) create a categorized corpus.
In the corpus, the filenames follow the format of YYYY-NDOCNUMB.txt, 
e.g. 1994-N1234567.txt

Clean files in unscrs_clean.zip
Renamed files in unscrs_renamed.zip
Categorized files in unscrs_renamed_categorized.zip
'''


import os
import glob

# 1. Explore text: 
# Here I define a function to explore the text of the documents to validate my logic.
# This is a quick way to understand in what collocations phrases are typically used
# and what kinds of topics they tend to reference. 

# Files contained in unscrs_clean.zip

def explore(strings):
    for filename in glob.glob('*.txt'):
        for line in open(filename):
            if strings in line:
                print line
                print filename # becomes very useful later to see which kinds of files the text is found in
    

# For example, actions the SC authorizes:
explore("authorizes")
# Phrases used in relation to arms embargoes:
explore("States shall prevent")
# Phrases used in relation to economic sanctions:
explore("economic activities")

''' The format of most SCRs is as follows: the first part outlines general positions
of the Council on certain things, using verbs in gerund form ("welcoming", "noting"),
while the second part states decisions taken, with verbs in the present tense ("decides",
"urges"). Most substantive actions are described in the first 1-3 points of the second part;
typically, if a resolution authorizes the deployment or extension of a mission or some
other kind of UN delegation/body, this will be stated first. 
'''
# Here I validate the logic described above.
explore("Decides")
# Here I make an educated guess that anytime "under Chapter VII" is used, it will
# always be in the context of "acting under Chapter VII (...)" and always in reference
# to a mission authorized to use force in situations of crisis.
explore("under Chapter VII")

# Further text exploration
explore("use all necessary means") # authorizing military personnel to shoot in defense of civilians
explore("drawdown") # drawing down missions
explore("Decides to extend") # extending a mission's mandate
explore("prevent the entry into or transit through their territories") # enacting travel bans 

# 2. Find files of interest based on text data, append their filenames to a list.
# Note: I can't create an empty list within the function, otherwise an existing list
# to which I would like to append other filenames based on other phrases found within
# will be overwritten every time.
def find_files(lists, expressions):
    for filename in glob.glob('*.txt'):
        for line in open(filename):
            if expressions in line:
                print filename # included for reference, to give an idea of how many there are and from what years
                lists.append(filename)
    print lists
    
# 3. Determine how to categorize files:
# Thinking also about how to structure the code that will distribute these files
# by category or "bin" within the directory in order to later build the categorized
# corpus.
    
# Thematic organization
# Soft measures
police = "police_" # civilian police component
embargo = "emb_" # embargoes
adv_team = "adv_team_" # advance teams
observers = "mil_observ_" # military observers
ban = "transit_ban_" # transit ban - sanctions
experts = "experts_" # establishment of panels of experts
fund = "fund_" # establishment of trust fund for operations
office = "office_"

# Chapter VII mission
chapter7 = "ch7_" # deployment of missions with military personnel under Chapter VII

# Mission extension
extend = "extend_" # extending mission mandates

# Drawdown, reversal of measures
drawdown = "drawdown_" # mission drawdown, termination of previously imposed measures
suspend = "suspend_" # suspend prohibitions

# Everything else will be read as "no action taken". Currently this seems to be
# about 280 documents out of the corpus (~1,250 total).

# 4. Rename the files by category, based on whether their filenames are in a given topical list:
def rename_files(list_name, var_name):
    for filename in os.listdir("."):
        if filename in list_name:
            os.rename(filename, var_name+filename)
            print filename # same as above, included for reference


''' Categorization '''

# I. Mission Extension
explore("Decides to extend")
explore("extend the present mandate")
explore("extend its mandate")
explore("decides to extend")
explore("Approves the continuation of")

mission_extend = []
find_files(mission_extend, "renew the mandate")
find_files(mission_extend, "extend its mandate")
find_files(mission_extend, "adjust the mandate")
find_files(mission_extend, "Decides to extend")
find_files(mission_extend, "Decides, in this context, to extend")
find_files(mission_extend, "Extends the stationing")
find_files(mission_extend, "Decides to renew for a period of")
find_files(mission_extend, "Authorizes the expansion of M")
find_files(mission_extend, "Approves the expansion of M")
find_files(mission_extend, "decides to extend")
find_files(mission_extend, "Decides to renew the mandates")
find_files(mission_extend, "increase the overall force levels")
find_files(mission_extend, "Approves the continuation of")

rename_files(mission_extend, extend)

# II. Mission Drawdown
explore("drawdown")
explore("terminate the mandate of")

mission_drawdown = []
find_files(mission_drawdown, "drawdown")
find_files(mission_drawdown, "gradual reduction of")
find_files(mission_drawdown, "Decides to withdraw U")
find_files(mission_drawdown, "liquidation")
find_files(mission_drawdown, "terminate the mandate of")

explore("Decides to terminate the prohibitions")
explore("Decides to terminate the remaining prohibitions")

suspend_prohib = []
find_files(suspend_prohib, "Decides to terminate the prohibitions")
find_files(suspend_prohib, "Decides to terminate the remaining prohibitions")

rename_files(mission_drawdown, drawdown)

rename_files(suspend_prohib, suspend)

# III. Deployment/Authorization to act under Chapter VII
explore("under Chapter VII")
ch7 = []
find_files(ch7, "under Chapter VII")
rename_files(ch7, chapter7)

# IV. Soft Measures
explore("civilian police")
civ_police = []
find_files(civ_police, "civilian police")
rename_files(civ_police, police)

explore("military observers")
military_observers = []
find_files(military_observers, "military observers")
rename_files(military_observers, observers)

transit_ban = []
find_files(transit_ban, "prevent the entry into or transit through their territories") 
rename_files(transit_ban, ban)
find_files(transit_ban, "States shall prevent")
rename_files(transit_ban, ban)
# note that these are mostly measures that go hand in hand with Chapter VII missions.

explore("the measures on arms")
arms_embargo = []
find_files(arms_embargo, "the measures on arms")
rename_files(arms_embargo, embargo)

explore("advance team")
advance_team = []
find_files(advance_team, "advance team")
rename_files(advance_team, adv_team)

explore("Panel of Experts")
panel_experts = []
find_files(panel_experts, "Panel of Experts")
rename_files(panel_experts, experts)

explore("trust fund")
trust_fund = []
find_files(trust_fund, "trust fund")
rename_files(trust_fund, fund)

sg_office = []
find_files(sg_office, "Requests the Secretary-General to establish the")
rename_files(sg_office, office)

# Other data explorations
explore("States shall prevent")
explore("increase the overall force levels")
explore("disarmament, demobilization and reintegration")
explore("targeted sanctions")
explore("use all necessary means")

# Renamed files saved in unscrs_renamed.zip

# 5. Separate files into one of two folders by category
# Define a function for this
import shutil
source = r"/Users/alex/Desktop/datsci/UN/corpus/unscrs_renamed"
destination = r"/Users/alex/Desktop/datsci/UN/corpus/unscrs_renamed/chapter_7"

def move_files(destination, word):
    if not os.path.exists(destination):
        os.makedirs(destination)               
    for f in os.listdir(source):
        if word in f:
            shutil.move(os.path.join(source,f), destination)

# Move all files whose filenames contain "ch7" to a folder called "chapter_7"
move_files(r"/Users/alex/Desktop/datsci/UN/corpus/unscrs_renamed_categorized/chapter_7", "ch7") # 523 files

# Move all other files to a folder called "soft_action"
# Use the first digit of the year contained in the filename to select and move these files
move_files(r"/Users/alex/Desktop/datsci/UN/corpus/unscrs_renamed_categorized/soft_action", "1")
move_files(r"/Users/alex/Desktop/datsci/UN/corpus/unscrs_renamed_categorized/soft_action", "2")
# total: 780 files

'''
Next steps:
1. Using previously assembled CSV file, match resolutions by number to category: 
- create a new "category" column 
- read resolution files using glob
- each file will contain the resolution number
- if the file is in the folder "soft_action", write "0" to the corresponding cell in the "category" column
- if the file is in the folder "ch7", write "1" 
- for all others, write "NaN" and drop with pandas
2. Read the text of each input (meeting record) into the corresponding cell in a new dataframe column
3. Select model(s), train & test 
'''

# Testing the creation of a categorized corpus reader on UNSCRs only
from nltk.corpus.reader import CategorizedPlaintextCorpusReader
reader = CategorizedPlaintextCorpusReader('/Users/alex/Desktop/datsci/UN/corpus/unscr3_renamed_categorized/', r'.*\.txt', cat_pattern=r'(\w+)/*')

reader.categories() 

categories = reader.categories()

# see http://stackoverflow.com/questions/15611328/how-to-save-a-custom-categorized-corpus-in-nltk?lq=1 
# for corpus installation instructions


