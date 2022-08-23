
from random import randint


num_of_dice = input ("How many times would you like to roll the dice? ")
# 1 2 3 4 5 6 
results = []
for i in range (int(num_of_dice)):
    results.append(randint(1,6))

for result in results:
    print(result, end = ' ')

print ("\nThen the sum of your rolled dice:",sum(results))

