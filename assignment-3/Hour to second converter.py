
option =print("please choose your option: \n1-convert houre to seconds \n2-convert seconds to hours ")
choice = int(input("your option is:"))

while True:

    if choice == 2 :
        num = int (input("now give us secods you need to convert: "))
        hour= num//3600
        b=num-3600*hour
        minutes=b//60
        seconds=b-60* minutes
    
        print(f"{hour}:{minutes}:{seconds}")

    elif choice == 1:
        num = input("now give us hours you need to convert( like this HH:MM:SS): ")
        seconds = 0 
        for part in num.split(':'):
            seconds= seconds*60 + int(part, 10)

        print("The seconds: " , seconds)
        break


    else :
        print("the choice you Entered is wrong!\nplz checked options")




    