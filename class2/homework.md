# Class 2 Homework

**Data Structure**

* column 1 - the ordinal of the order
* column 2 - the quantity of the item requested in the order
* column 3 - item name
* column 4 - what/whether choices/options were requested by the customer
* column 5 - price of items

There were 1,834 orders placed. 

Code used: `head chipotle.tsv` 

There were 4,623 lines in the files.

Code used: `wc -l chipotle.tsv`

* Using 
```
grep -i "chicken burrito" chipotle.tsv | wc -l
```
we found that there were 553 orders of chicken burritos.
* Using
``` 
grep -i "steak burrito" chipotle.tsv | wc -l
```
we found that there were 368 orders of steak burritos. Chicken thus appears to be more popular, *bawk bawk bawk*.

* Using
```
grep -i "chicken burrito" chipotle.tsv | grep -c -i "black beans"
```
we found that there were 282 orders of chicken burritos with black beans.

* Using 
```
grep -i "chicken burrito" chipotle.tsv | grep -c -i "pinto beans"
```
we found that there were 105 orders of chicken burritos with pinto beans. This matches previously held assumptions that **black beans are clearly superior**.

We can double check these numbers by running 
```
grep -i "chicken burrito" chipotle.tsv | grep -i "black beans" | wc -l
```
and the same for pinto beans, which returns the same numbers (282 & 105 respectively).

* Using
```
find . -name *.*sv
```
we can find all files in DAT7 ending in .csv or .tsv. There are three:

./data/airlines.csv
./data/chipotle.tsv
./data/sms.tsv

* Using
```
grep -r -i "dictionary" . | wc -c
```
we see that there are 1,611 instances of the word "dictionary", regardless of case, in all DAT7 files.

**Interesting Info**

1. 101 orders for sides of chips were placed.

```
grep -i "side of chips" chipotle.tsv | wc -l
```

2. That said, chips in some form were ordered 1,084 times.

```
grep -i "chips" chipotle.tsv | wc -l
```

3. Using the same grep command, bowls were ordered 1,331 times, burritos 1,172 times, and salads 195 times. 

*To resolve*:

*Can't quite figure out how to calculate the average cost of an order using awk. For example, the code below works on columns 1 & 2, but not on column 5, presumably because it's presented with a $ sign?*
```
awk '{ sum += $2; n++ } END { if (n > 0) print sum / n; }' chipotle.tsv
```
*ETA*: using csvstat explained why awk wasn't working; item_price is `<type 'unicode'>`, whereas order_id & quantity are `<type 'int'>`. 


