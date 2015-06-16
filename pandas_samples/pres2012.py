# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 23:49:10 2015

@author: alex

Visualization & Pandas practice with
2012 French presidential election data (first round)
See end of code for data description

"""
import pandas as pd
import matplotlib.pyplot as plt

# read in the drinks data
pres_cols = ['dep', 'eco1', 'fn', 'ump', 'gdiv1', 'ug1', 'ug2', 'ug3', 'centr', 'ddiv1', 'ps']
pres = pd.read_csv('pres2012.csv', header=0, names=pres_cols, na_filter=False)

# general info, numeric values of top candidates
pres.shape
pres.ump.describe()
pres.ps.describe()
pres.fn.describe()

# where did each of the top 3 candidates do best/worst?
pres[pres.ump > 30.0].dep
pres[pres.ps > 30.0].dep
pres[pres.fn > 25.0].dep

# select admin unit & votes as %, put in new DF
ump_df = pres.loc[:, ['dep', 'ump']]
# top 10 UMP
ump_df.sort('ump', ascending=False).head(10)

# top 10 PS
ps_df = pres.loc[:, ['dep', 'ps']]
ps_df.sort('ps', ascending=False).head(10)

# top 10 FN
fn_df = pres.loc[:, ['dep', 'fn']]
fn_df.sort('fn', ascending=False).head(10)

# performance in Paris
pres[pres.dep=="PARIS"]

''' VISUALIZATION '''

pres.ump.plot(kind='hist', bins=20)
pres.ps.plot(kind='hist', bins=20)
pres.fn.plot(kind='hist', bins=20)

pres[['ump', 'ps']].sort('ump').values
pres.plot(kind='scatter', x='ps', y='ump') # fits hypothesis: higher UMP votes, lower PS votes
pres.plot(kind='scatter', x='ump', y='fn') # line not as evident; but votes may have been interchangeable

# demonstration of vote distribution relationships between binomes
pd.scatter_matrix(pres[['ump', 'ps', 'fn']], figsize=(10, 8))

pres[['ump', 'ps', 'fn']].plot(kind='hist', stacked=True)

# testing hypothesis of voters "so far on the left they come out on the (far) right"
pd.scatter_matrix(pres[['fn', 'ug1', 'ug2']], figsize=(10, 8))
# ^^ it works!

pd.scatter_matrix(pres[['fn', 'ug2', 'ug3']], figsize=(10, 8))


'''
Data source: http://data.gouv.fr

Data desc: 

dep = department (administrative unit)
eco1 = Eva Joly, environmental party candidate
fn = Marine Le Pen, far-right nationalist candidate
ump = Nicolas Sarkozy, rightist candidate, incumbent
gdiv1 = Jean-Luc Melenchon, leftist candidate
ug1 = Philippe Poutou, far-left candidate (1)
ug2 = Nathalie Arthaud, far-left candidate (2)
ug3 = Jacques Cheminade, far-left candidate (3)
centr = Francois Bayrou, centrist candidate 
ddiv1 = Nicolas Dupont-Aignan, rightist candidate
ps = Francois Hollande, socialist candidate, primary challenger

'''