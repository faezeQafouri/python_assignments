
psw = "7229"
report_to_police = "9227"
cnt = 4
while True:
    ATM = int(input("Enter your pass card:"))

    if ATM == psw :
        print ("welcome , Do what you want :D")
        break

    elif ATM != psw  and len(str(ATM)) !=4 :
            print (" your password is not correct!, try again \nplease enter your password  in four digit here ")
            continue

  
    elif   ATM == report_to_police  : 
         print (" heh is it over? It was very impressive :] \nOpen the door, the police are waiting for you :)))")
         break

    else:   
         
         cnt -= 1
         if cnt == 1 :
                print("\n your cart blocked!! Due to Entering Wrong Password")
                break
       
         else:
                print (" you have got",cnt-1,"more tries" )
                continue

    



    
