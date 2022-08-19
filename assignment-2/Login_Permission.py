import os 
os.system('cls')


# if username server = username client ,  then welcome 

user = "faeze"
psw = "9731"
cnt = 0
while  cnt < 3 :
 user1 = input("plz enter your username:")
 psw1 = input("plz enter your password:")

 if user1 == user and psw1==psw :
     print (" Hi , welcome" , user1)
     break

 elif user1 != user  or  psw1 != psw :
     cnt+=1
                    
     if  user1 == user  and  psw1 != psw :
             print("try again !! .. your  Password its not correct")  
             continue            
                                    
     elif user1 != user and psw == psw1 :
             print ("try again !! your  usename its not correct ")
             continue

     else :
         print ("Your username and passwords not correct !!  ")     
                           
 if  cnt == 3 :
    print ("You're Account has been Locked plz try again in 30s later  .... ")
    break
                        

 

   
    
    


