


def math (string):
     
    
    # operator ='+-*/**//'
    # res=""
    # for i in string:
    #     if i in operator:
    #          res+="--"+i+"--"
    #     else:
    #          res+=i

    # res=res.split("--")

    # while ''in  res :
    #     res.remove('')
   #------------------------------------------------------------ 
    operator = ['+','-' ,'*','/', '**','//']
    operators = []

    #Add operators to the list to check   
    for letter in string :
        for i in range(6):  
            if letter == operator[i]: 
                operators.append(letter)
    #---------------------------------------------------  
    for i in range(6):
         mathematical_phrase = string.split(operator[i])
         string = ' '.join(mathematical_phrase)
    
    mathematical_phrase = string . split(' ')

    while ''in mathematical_phrase :
        mathematical_phrase.remove('')

    #------------------convert string to int for calculate pharase---------------------------------
        
    for i in range(len(mathematical_phrase)):

        mathematical_phrase[i] = int (mathematical_phrase[i])
     #---------------------------------------------------------------
     
    counter = 0  
    while '*' in operators  or  '/' in operators:
        
        if operators[counter] == '*':
            
            mathematical_phrase[counter] = mathematical_phrase[counter] * mathematical_phrase[counter+1]
            
            mathematical_phrase.pop(counter+1) 
            operators.pop(counter)
            
            counter -= 1
            
        
        elif operators[counter] == '/':
            
            mathematical_phrase[counter] = mathematical_phrase[counter]/mathematical_phrase[counter+1]
            
            mathematical_phrase.pop(counter+1) 
            operators.pop(counter)

            counter -= 1
    
        
            
        counter += 1
           
    counter = 0 
        
    while '+' in operators or  '-' in operators:   
            
        if operators[counter] == '+':
            
            mathematical_phrase[counter] = mathematical_phrase[counter]+mathematical_phrase[counter+1]
            
            mathematical_phrase.pop(counter+1) 
            operators.pop(counter)
            
            counter -= 1
            
        
        elif operators[counter] == '-':
            
            mathematical_phrase[counter] = mathematical_phrase[counter]-mathematical_phrase[counter+1]
            
            mathematical_phrase.pop(counter+1) 
            operators.pop(counter)

            counter -= 1
    
        
            
        counter += 1 

    counter = 0

    while '**' in operators or  '//' in operators:   
            
        if operators[counter] == '**':
            
            mathematical_phrase[counter] = (mathematical_phrase[counter]) ** (mathematical_phrase[counter+1]
            )
            mathematical_phrase.pop(counter+1) 
            operators.pop(counter)
            
            counter -= 1
            
        
        elif operators[counter] == '-':
            
            mathematical_phrase[counter] = (mathematical_phrase[counter]) //( mathematical_phrase[counter+1])
            
            mathematical_phrase.pop(counter+1) 
            operators.pop(counter)

            counter -= 1
    
        
            
        counter += 1 
        
        

    
        
    
    # printing result   for first list if you want to convert all phrase to list 
    # print("The list after performing split functionality : " + str(res))

    

phrase = input ("Enter your desired mathematical expression:")
math (phrase)
