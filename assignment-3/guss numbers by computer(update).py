import random
from typing import Counter

print ("Consider a number between 0 and 99 in your mind ")

print("wainting for me , im thinking ... ")
lowest_num= 0 
highest_num = 99

print ("please choose (lower) , (higher) or (yes) for answering the questioins")
AL_guess = random.randint(lowest_num,highest_num)
print ('Is your number ',AL_guess ,'?')
resualt = input()  


  

 
    
counter_guss = 1
while  resualt != 'yes':
      
     if resualt =='lower':
               highest_num = AL_guess-1
               AL_guess = random.randint(lowest_num,highest_num)
               print ('Is your number ',AL_guess ,'?')
               resualt = input()
               counter_guss+=1
               


     else :
               lowest_num = AL_guess+1
               AL_guess = random.randint(lowest_num , highest_num) 
               print ('Is your number ',AL_guess ,'?')
               resualt = input()
               counter_guss+=1
               


    
            
print ("heeeeeeeeey AL win :D")
print ('I was able to guess the number after '+str(counter_guss)+ ' times')
          
    

        
