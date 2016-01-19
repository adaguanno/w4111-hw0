# Ashley Daguanno
# Homework 0 
# UNI: ad3079

count = 0
key = 'single malt scotch'

with open('iowa-liquor-sample.csv') as f:
    for line in f:
        cur = line.lower()
        if key in cur:
           count = count + 1

print (count)

