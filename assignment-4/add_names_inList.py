import time



Qty = int(input ("Enter the Qty of names:"))

names = []
for i in range (1 , Qty+1):
    name = input("Enter a name "+str(i)+": ")
    names.append(name)


print("\tThe list of your Entered names:" ,names)


for i in range (1,4):
    element = input("\bEnter a names you want to add :")
    
    # Element to be inserted before 3
    beforeElement = input("\bEnter a name you want to add before :")
    
    # Find index
    index = names.index(beforeElement) 
    
    # Insert element at beforeElement 
    names.insert(index, element) 
    print('\t',names)
         
                     
                
    
    