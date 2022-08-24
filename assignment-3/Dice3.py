
import random

results = []
counter = 0 

#chra while ? chon nemidonim chand bar tas mindaze ta 6 biare!
while True :
      num_of_dice = random.randint(1,6)
      results.append(int(num_of_dice))

# for checking an elements in Lists we use -> in <- 
      if 6 in results :
         counter+=1
         continue
         
         
            
      else : 
        print("Numbers of rolled dice= ",results, end = ' ' )
        print ("\nThen the sum of your rolled dice:",sum(results))
        break
         
        

print ("The times that dice were thrown until the number 6 appeared:  ", counter)

# Repitation_times =results.count(6)
# print(Repitation_times)

