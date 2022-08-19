
import os 
os.system('cls')



num = int (input("enter a number you want: "))
odd_cnt=0
even_cnt =0

while num!=0 : 

    result= num % 10 
    num = num // 10

    if num % 2 == 0 :
        even_cnt+=1
    else: 
        odd_cnt+=1 

print ("\n Even digit :" , even_cnt , "\n odd digit : " , odd_cnt )
if even_cnt > odd_cnt :
    print ("\n Even digits are  more than  Odd digit  " )
elif even_cnt < odd_cnt : 
    print ("\n Odd digits are  more than  even digit ")
else :
    print ("The number of even digits is equal to odd digits")