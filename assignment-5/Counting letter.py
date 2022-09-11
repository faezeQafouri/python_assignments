
from tabulate import tabulate
from termcolor import colored

# print ( '\033[1m' + '---------- Welcome to counting letter ----------' + '\033[0m')
# info = {'You can choose:': ['1) one sentence', '2) Several sentences']  }
# print(tabulate(info, headers='keys', tablefmt='fancy_grid') )

# choice =int(input('\033[33;1m'+'choice: '+'\033[30;1m'))

# if choice == 1 :

def counting_letter (string):

        char = len(string)
        print(colored("There are " + str(char) + " letter." , 'blue'))
        #-------------------------------------------------------------------
        word = len(string.split())
        print(colored("There are " + str(word) + " words." , 'yellow'))
        #-------------------------------------------------------------------
        for i in range(len(string)):
            counter = string.count(string[i])
            # if string[i] == ' ':
            #         string[i] = 'space'
            #         str= ''.join(string[i])
            # print (string[i], counter)
            print ("\033[1;34m" + string[i],'=',string.count(string[i]),'|', end=" " + "\033[0m")
        #--------------------------------------------------------------------
        counter1 = 0
        for i in string:
            if i == ' ' or i == '\n':
                 counter1 += 1
        print(counter1)
        print(colored("There are " + str(counter1) + " space + enter." , 'yellow'))
        #---------------------------------------------------------------------

        comma = len(string.split(','))
        print(colored("There are " + str(comma) + " comma's." , 'blue'))

        #----------------------------------------------------------------------
        dots = len(string.split(','))
        print(colored("There are " + str(dots) + " Dots." , 'yellow'))

        #----------------------------------------------------------------------

        character=string.count(',')+string.count('.')+string.count(' ')
        print(colored("There are " + str(character) + " comma+ dots+ space ." , 'blue'))



        

str1 = input("Enter your desire sentence: ")
counting_letter(str1)

