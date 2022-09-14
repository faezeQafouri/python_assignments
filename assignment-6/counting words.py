from termcolor import colored

def countingWords (string ):
    alphabets = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" ,
                     "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"] 

    element=["." , "," , "/" , "//" , "[" , "]" , "{" , "}" , "!" , "#" , "&" , "(" , 
                ")" , "*" , "^" , ":" , ";" , "\'" , "\"" , "<" , ">" , "|" , "$" , "%" ,
                 "~" , "`" , "@" , "?" ]



    for elments in element:
        # replace  in string is the same remove function in list
         string= string.replace(elments , " ")

    counter = 0
    for letter in string:
        if letter in alphabets:
            counter +=1 

    print (colored("There are "+str(counter)+ " letters in the sentence you enterd." , 'green'))


    word = len(string.split())
    print(colored("Then " + str(word)+ " words in this sentence. " , 'yellow'))


text = input("Enter your desier sentence :")
countingWords(text)