import os 
os.system('cls')


num = int (input(" plz enter a number: "))
temp = num
reverse = 0 
while num !=0 :
     remainder = num % 10 
     reverse = reverse * 10 + remainder
     num = num // 10 

#print ('\033[1;37mciao!') ---> for bolding text 

print ("\033[1;37mnumber in initial state:" , temp  )
print ("\033[1;37mnumber in reverse  state:" , reverse )

if temp != reverse:
    print (" ..... The number and its inverse are not equal :( ...... ")
else:
    print ("...... The number and its inverse are equal :) ........ ")

