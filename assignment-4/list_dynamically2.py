
import random 
import os 
os.system('cls')


num_of_list = int(input ("Enter number of numbers you want to be in the list: "))
list1 = []

for i in range(num_of_list):
     list1.append(random.randint(0, 140))
     

print ("\nThe list you created:" , list1 ) 