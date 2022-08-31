

names = [ 'ali','atefe','homa','amir','fateme']


for i in range (1,4):

    element = input("\bEnter a names you want to add :")
    
    # Element to be inserted before
    beforeElement = int(input("\bwhich number do you want in queue  :"))
    
    #list.insert(index,item)
    names.insert(beforeElement-1,element) 
    print('\t',names)
         