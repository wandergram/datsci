# Class 3 Chipotle homework
# Ex 1
import csv
with open('chipotle.tsv', 'rU') as f:
    data = [row for row in csv.reader(f, delimiter='\t')]

# Ex 2
header = data[0]
data = data[1:]

# Ex 3
# Step 1: cleaning the prices
prices = [row[4] for row in data]
new_prices = []
for price in prices:
    if "$" in price:
        clean_price = price.strip("$")
        new_prices.append(round(float(clean_price), 2))
# print new_prices - checking to make sure

# Step 2: sum up prices
cost_total = sum(new_prices[0:])

# cost_total prints out to 34500.16

# Step 3: sum up quantities
quantities = [float(int(row[1])) for row in data] 
# float was important here because otherwise reading it as an integer messed up
# further calculations down the line
quant_total = sum(quantities[0:])

#quant_total prints out to 4972

# divide total cost by total quantities
cost_by_quant = cost_total / quant_total
# cost_by_quant = 6.9388 = average cost of an item

# divide quantities by order
quant_by_order = round(float(quant_total / 1834), 10)
# orders had 2.7 items on average

avg_order_cost = cost_by_quant * quant_by_order
# prints out to 18.81 - this seems high; maybe something's off 
# with the logic here?

# Ex 4:

mydict = {}
for row in data:
    k = row[2]
    v = row[3]
    if not k in mydict:
        mydict[k] = [v]
    else:
        mydict[k].append(v)

# the commented out code below was only printing a subset of the data;
# haven't figured out why yet. The code above created a huge dictionary,
# but seemed to work... ?

#dict = {}
#for row in data:
    #dict[row[2]] = row[3]

sodas = []
everything_else = []
for key, value in mydict.items():
    if "Canned" in key:
        sodas.append(value)
    else:
        everything_else.append(value)
        
import itertools # creative workaround to flatten list of lists?
merged_sodas = list(itertools.chain(*sodas))
count = 0
for x in merged_sodas:
    count += 1

print count # 405 sodas total No idea why I did this. 

set(merged_sodas) # FINALLY WE HAVE A SET OF SODAS. This took embarrassingly long.

'''
{'[Coca Cola]',
 '[Coke]',
 '[Diet Coke]',
 '[Diet Dr. Pepper]',
 '[Dr. Pepper]',
 '[Lemonade]',
 '[Mountain Dew]',
 '[Nestea]',
 '[Sprite]'}
 '''

# Ex 5
# Same initial logic as above: create dictionary with row[2] and row[3],
# select keys containing "burrito", calculate length of values,
# calculate burrito total, calculate total length of values, divide.

burrito_dict = {}
for row in data:
    k = row[2]
    v = row[3]
    if not k in burrito_dict:
        burrito_dict[k] = [v]
    else:
        burrito_dict[k].append(v)
    
toppings = []
topsum = []
for key, value in burrito_dict.items():
    if "Burrito" in key:
        for x in value:
            tops = x.count(',')
            topsum.append(tops)

totaltops = sum(topsum)
print totaltops

# 5151 toppings total

        

''' 
Experimental zone of non-working list-flattening code:

the code below doesn't work with the structure of this list of lists, because
testing the result using a basic counter gives us a count of 1172 - same as burrito count
len(toppings) still gives us 6, probably because of lists nested within lists. This was
probably because of how I handled the construction of the dictionary above.
       
import itertools # creative workaround to flatten list of lists?
merged_toppings = list(itertools.chain(*toppings))
# merged_toppings2 = list(itertools.chain(*merged_toppings)) - this doesn't work
# as a second-level list flattener because it sepearates all characters

# [... for inner_list in outer_list for item in inner_list]
'''

kind_of_items = [row[2] for row in data]
burrito_total = []
for item in kind_of_items:
    if "Burrito" in item:
        burrito_total.append(item)

print burrito_total
len(burrito_total) # total of 1172 burritos
        
tops_per_bur = totaltops / round(float(len(burrito_total)), 2)
print tops_per_bur

# 4.39 toppings per burrito

# Ex 6
# Logic similar to above, realized that the if not statement allows you to discard
# repeat keys, which turned out to be very useful in this situation.
# defaultdict gave errors... 

chip_dict = {}
for row in data:
    if "Chips" in row[2]:
        key, value = row[2], row[1]    
        if not key in chip_dict:
            chip_dict[key] = [value]
        else:
            chip_dict[key].append(value)
    
for key, value in chip_dict.items():
    values = sum(map(int, value))
    chip_dict[key] = values
    
'''
Output

{'Chips': 230,
 'Chips and Fresh Tomato Salsa': 130,
 'Chips and Guacamole': 506,
 'Chips and Mild Fresh Tomato Salsa': 1,
 'Chips and Roasted Chili Corn Salsa': 23,
 'Chips and Roasted Chili-Corn Salsa': 18,
 'Chips and Tomatillo Green Chili Salsa': 45,
 'Chips and Tomatillo Red Chili Salsa': 50,
 'Chips and Tomatillo-Green Chili Salsa': 33,
 'Chips and Tomatillo-Red Chili Salsa': 25,
 'Side of Chips': 110}
 '''


# Unused code

'''
import collections 
new_chips = collections.defaultdict(list)
for key, value in chip_dict:
    new_chips[key].append(value)
'''



