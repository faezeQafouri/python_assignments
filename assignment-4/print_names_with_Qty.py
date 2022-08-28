from collections import Counter
qty = int(input("Enter Qty of names , you want to : "))

list= []
for i in range (1 , qty+1):
     x = input ("plz enter a name :"+str(i)+":")
     list.append(x)
# print(Counter(list))


# To get the number of occurrences
# of each item in a dictionary
print (dict( (l, list.count(l) ) for l in set(list)))