# Ashley Daguanno
# Homework 0 
# UNI: ad3079

count = 0
key = 'single malt scotch'

with open('iowa-liquor-sample.csv') as f:
    for line in f:
        attributes = line.split(",")
        catName = attributes[12].lower()
        descrip = attributes[16].lower() 
        # descrip not 100% necessary -- check in case key is not in catName
        if key in catName or key in descrip:
           count = count + 1

print (count)


"""
# alternate code that just treats each line as a string and
# does a substring search
with open('iowa-liquor-sample.csv') as f:
    for line in f:
        cur = line.lower()
        if key in cur:
           count = count + 1

print (count)
"""
