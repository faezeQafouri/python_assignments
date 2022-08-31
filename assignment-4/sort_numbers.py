
from unittest import result


Results=[]
list= []
for i in range (1,11):
    x = float(input ("plz enter a number " +str(i)+ ":"))
    list.append(x)
    


for i in range (1 , len(list)):
    if list[i-1]<list[i]:
        temp = True
        Results.append(temp)
        continue
    elif list[i-1]==list[i]:
        temp = 'equal'
        Results.append(temp)
    else:
        temp = False
        Results.append(temp)

for i in range (1 , len(Results)):
    
    if Results[i-1]==Results[i] and Results[i-1]=='equal':
        temp1='equal'

    elif Results[i-1]==Results[i]:
           temp1 = "yes"
      
    else:
       temp1 = "No"



if temp1 == "yes":
    print ("YES ")

elif temp1=="equal":
    print("the numbers you Entered are equal (for example: 2,2,2,..)")
else : 
    print("NO")