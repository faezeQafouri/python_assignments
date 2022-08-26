import math

number = int(input("please Enter integer number: "))
Divisor = []


for i in range (1,number) :
    temp = number % i 
    if temp == 0 :
        print(i)
        Divisor.append(i)
    else :
        i+=1

    
for i in Divisor   :
    if i < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        result = math.factorial(i)
        if result == number:
            # outcome= True
            print("YES , The factorial of {} is: {}".format(i, result))
               
        else :
            # outcome= False
            # continue 
             print("NO , This number is not a numerical factorial ")  
           

# if outcome == True:
#     print("YES , The factorial of {} is: {}".format(i, result))

# else :
#      print("NO , This number is not a numerical factorial ") 

 

             
