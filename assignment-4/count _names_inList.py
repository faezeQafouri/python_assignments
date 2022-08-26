



Qty = int(input ("Enter the Qty of names:"))

names = []
for i in range (1 , Qty+1):
    name = input("Enter a name "+str(i)+": ")
    names.append(name)

print("The list of your Entered names:" ,names)


# while Qty>= 0 :
counter = 0 
for i in range(Qty):
    for j in range(i+1 , Qty):
    
    # finding the index
    # with same value but
    # different index.
         if (names[i] == names[j] or names[j]== names[i]):
            counter += 1
    print(names[i] , "Number of repetitions =" , counter)
         
                     
                
    
    