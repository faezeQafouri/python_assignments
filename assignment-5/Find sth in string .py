
from tabulate import tabulate
from termcolor import colored

# print ( '\033[1m' + '---------- Welcome to counting letter ----------' + '\033[0m')
# info = {'You can choose:': ['1) one sentence', '2) Several sentences']  }
# print(tabulate(info, headers='keys', tablefmt='fancy_grid') )


def counting_letter (string):


        #counting charactor
        char = len(string)
        print(colored("There are " + str(char) + "characters." , 'blue'))

        #counting letter 
        alphabets = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" ,
                     "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"] 
        counter_letter =0
        for letter in string :
            if letter in alphabets:
                counter_letter+=1

        print(colored("There are " + str(counter_letter)+ " letter." , 'yellow'))

        #counting words 
        word = len(string.split())
        print(colored("There are " + str(word)+ " words." , 'blue'))

        #count each of letter in string 
        for i in range(len(string)):
            counter = string.count(string[i])
            # if string[i] == ' ':
            #         string[i] = 'space'
            #         str= ''.join(string[i])
            # print (string[i], counter)
            print ("\033[1;34m" + string[i],'=',string.count(string[i]),'|', end=" " + "\033[0m")
        #--------------------------------------------------------------------
        counter1 = 0
        counter2 = 0
        for i in string:
            if i == ' ' :
                 counter1 += 1
            elif  i == '\n':
                counter2 += 1

        
        print(colored("There are " + str(counter1) + " space." , 'yellow'))
        print(colored("There are " + str(counter2) + " enter." , 'yellow'))
        #---------------------------------------------------------------------

        comma = len(string.split(',')) +len(string.split(';'))
        print(colored("There are " + str(comma) + " Semicolons and comma's." , 'blue'))

        #----------------------------------------------------------------------
        dots = len(string.split('.'))
        print(colored("There are " + str(dots) + " Dots." , 'yellow'))

        #----------------------------------------------------------------------

       


        

str1 = input("Enter your desire sentence: ")
counting_letter(str1)

