import random

print ("Consider a number between 0 and 99 in your mind ")
print("wainting for me , im thinking ... ")
lowest_num= 0 
highest_num = 99
number_list= []
AL_guess = random.randint(lowest_num,highest_num) 
number_list.append(AL_guess)
print ('Is your number ',number_list[0] ,'?')
resualt = input()
    
counter= 1
while True:
   for i in range (len(number_list)):
        
        if resualt == 'yes' :
                print ("heeeeeeeeey AL win :D")
                print ('The AI was able to guess the number after '+str(counter)+ 'times')
                break
        
        elif resualt == 'lower' :     
        
            
                AL_guess = random.randint(lowest_num,number_list[i]) 
                number_list.append(AL_guess)
                print ('Is your number ',number_list[i+1] ,'?')
                resualt = input()
                counter+=1

                if resualt == 'higher':
                    AL_guess = random.randint(number_list[i+1] , number_list[i]) 
                    number_list.append(AL_guess)
                    print ('Is your number ',number_list[i+1] ,'?')
                    resualt = input()
                    counter+=1
                    break

                else :
                    AL_guess = random.randint( lowest_num , number_list[i+1]) 
                    number_list.append(AL_guess)
                    print ('Is your number ',number_list[i+2] ,'?')
                    resualt = input()
                    counter+=1
                    break

        else :

            AL_guess = random.randint(number_list[i] , highest_num) 
            number_list.append(AL_guess)
            print ('Is your number ',number_list[i+1] ,'?')
            resualt = input()
            counter+=1