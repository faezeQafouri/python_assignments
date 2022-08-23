from ast import Num
import random 
import os 
os.system('cls')

list1 = []
list2 = []
n=20
for i in range(n):
     list1.append(random.randint(0, 50))
     

for num in list1 :
    num = num * num 
    list2.append(num)


print ("First list is:\n" , list1 ,"\nThe second list is:\n" , list2) 