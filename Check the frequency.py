
a = {"codingal" : 2 , "is" : 2 , "the" : 2,"best" : 1}

print("original dicnary is:" , a)

k = int(input("enter a number"))

res = 0

for key in a:
    if a[key] == k:
        res += 1

print("the number of frequency of the number" , k , "is" , res)