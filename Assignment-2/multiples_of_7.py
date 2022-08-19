

# if num % 7 == 0  print true 
# else Find the first 7-dimensional multiple of that number

import os 
os.system('cls')


num = int (input("Enter a number:"))
temp = num 

if num % 7 == 0 :
    print ("The number you entered is: " + str(num) + "  and its multiple of 7 :D ")
    

else :
    num % 7 != 0 
    num +=1 
    print("The number you Enter is: " + str(temp) +"\tIts not in multiples of 7 !! " ,"\nI showed the nearest number that was a multiple of 7:" , num )
        
