

n = int(input("List length = "))

list= []
for i in range (1 , n+1):
    x = int(input ("plz enter number"+str(i)+":"))
    list.append(x)
    
for i in range(len(list)):
    for j in range(i + 1, len(list)):

        if list[i] > list[j]:
            list[i], list[j] =list[j], list[i]


print("The sorted list is:",list)
