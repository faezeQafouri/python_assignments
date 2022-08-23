

import os 
os.system('cls')

list1 = [1 , 4, 76, 8, 34, 12, 20 , 7 , 14 , 21, 9 , 54, 36 , 79 , 110 , 5 , 27 ,112 , 201 , 67]
list2 = []
for num in list1 :
    num = num * num 
    list2.append(num)


print ("First list is:\n" , list1 ,"\nThe second list is:\n" , list2) 