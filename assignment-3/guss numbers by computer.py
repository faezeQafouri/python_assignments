import random
from typing import Counter

print ("Consider a number between 0 and 99 in your mind ")
print ("please choose lower , higher or yes for answering the questioins")
print("wainting for me , im thinking ... ")
lowest_num= 0 
highest_num = 99

AL_guess = random.randint(lowest_num,highest_num)
# print ('Is your number ',AL_guess ,'?')
# resualt = input()  

counter_guss = 1
counter_end = 0 
while counter_end == 0 :

    print ('Is your number ',AL_guess ,'?')
    resualt = input()  


    while True:

       if resualt == 'yes':
            
            print ("heeeeeeeeey AL win :D")
            print ('The AI was able to guess the number after '+str(counter_guss)+ ' times')
            counter_end =0
            break

       elif resualt =='lower':
             highest_num = AL_guess
             AL_guess = random.randint(lowest_num,highest_num)
             print ('Is your number ',AL_guess ,'?')
             resualt = input()
             counter_guss+=1
             continue


       else :
            lowest_num = AL_guess
            AL_guess = random.randint(lowest_num , highest_num) 
            print ('Is your number ',AL_guess ,'?')
            resualt = input()
            counter_guss+=1
            continue

    

        
