
psw = ['7','2','9','7']
report_to_police = ['9','2','2','7']
cnt = 4
while True:
    ATM = list(input("Enter your pass card:"))
     
    if psw==ATM:
          print("welcome , Do what you want :D")
          break
    elif ATM==report_to_police:
          print(" heh is it over? It was very impressive :] \nOpen the door, the police are waiting for you :)")
          break
    elif len(ATM)!=4:
        print(" your password is not correct!, try again \nplease enter your password  in four digit here ")
        continue   
    else:
      cnt-=1
      if cnt == 1 :
                print("\n your cart blocked!! Due to Entering Wrong Password")
                break
       
      else:
                print (" you have got",cnt-1,"more tries" )
                continue
      
