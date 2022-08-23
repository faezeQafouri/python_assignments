
from cgitb import reset
import random 


print ("Consider a number between 0 and 99 in your mind ")
print("wainting for me , im thinking ... ")
computer_guess = random.randint(0,99) 
print ('Is your number '+str(computer_guess)+'?')
resualt = input()
i=1
counter= 0 
while True:

    if resualt =='yes':
         print ("heeeeeeeeey AL win :D")
         print ('The AI was able to guess the number after '+str(counter)+ 'times')
         break

    elif resualt == 'lower':
         computer_guess1 = random.randint(0,computer_guess)
         temp =computer_guess1
         print ('Is your number '+str(computer_guess)+'?')
         resualt = input()
        #  if resualt =='lower':
        #      computer_guess3 = random.randint(0,computer_guess1)
        #      print ('Is your number '+str(computer_guess3)+'?')
        #      resualt = input()

        #  else :
                
                
         counter +=1
         continue

    elif resualt == 'higher':
         computer_guess2= random.randint(computer_guess,temp)  
         print ('Is your number '+str(computer_guess2)+'?')
         resualt = input()
         counter +=1
         continue
   
     


