from termcolor import colored
from tabulate import tabulate
import random 

def welcome ():
    name = input("""
                _______________________________________________________________________

                > Welcome to the Hangman Game! Please Enter your preferred game name:  <
                """).capitalize()

    if name.isalpha() == True:
        print(""">> Hi!""",name,"""Glad to have you here! <<<
                You will be playing against the computer today.
                The computer will randomly choose a word and you will try to guess what the word is.
                You can always invite your friends for a fun time together
                ==========================================================
                Good Luck! Have fun playing""" )

    else:
        print('\033[35mPlease enter your name using letter only \033[0m' )
        name = input('Enter a game name here:  ')
        print('\033[32mHi!',name,'Please go through the rules of the game below \033[0m ' )   

def play_again():
    
    """ This function asks user/player if he/she wishes to replay the hangman game """
    response = input("Would you like to play again? yes/no. Enter 'Y' for Yes or 'N' for No").lower()

    #Create a decision making process
    if response == 'y':
        game_run()
    else:
        print('Hope you had fun playing the game. See you next time')



def get_word():

    """ This function generates the word the user will attempt guessing"""


    info = {'category:': ['Food', 'Color', 'Computer','Body','Animall','Subjects','Sports','Things','Vegetable','Nature','Places'],
        'Your choice:': ['1', '2' ,'3','4','5','6','7','8','9','10','11']}
    print( colored( tabulate(info, headers='keys', tablefmt='fancy_grid') , 'yellow') )
    choice = int(input("we waiting for you .. :") )
        
    foods = ['hamburger','Caesar Salad','pizza','sushi','hotdog','kebab','ghormesabzi',
    'icecream','pasta','Beef Stroganoff','noodles','friedchicken']

    colors= ['red', 'green','blue','black','purple','gray','yellow', 'white','violet','golden']

    computer = ['monitor','mouse','controller','switch','speaker','keyboard','windows','stackoverflow']

    Body = ['Throat','Forearm','Pancreas','tangue','shoulder','teeth','thumb','Elbow','Stomach','Brain']

    animall = ['wolf','grasshoper','grollia','owl','butterfly','keyboard','eagle','caterpillar']

    subjects = ['monitor','mouse','controller','switch','speaker','keyboard','windows','stackoverflow']

    sports = ['basketball','swimming','soccer','chess','cycling','hockey','vollyball','bodybilding']

    things = ['candle','backpack','desk','television','padlock','briefcase','balloon','Swings']

    vegtebale = ['spinach','pumpkin','sweetcorn','scallion','lettuce','garlic','cabbage','mushroom','asparagus','radish']

    nature = ['rainbow','volcano','river','mountain','desert','Ocean','Waterfall','Valley']

    places = ['bedroom','corridor','library','supermarket','hospital','airport','skyscrapers','playground']



    if choice == 1 :
        final_answer = random.choice(foods).lower()
        return final_answer
    elif choice == 2 :
        final_answer= random.choice(colors).lower()
        return final_answer
        
    elif choice == 3 :
        final_answer= random.choice(computer).lower()
        return final_answer 
    elif choice == 4 :
        final_answer= random.choice(Body).lower()
        return final_answer 

    elif choice == 5 :
        final_answer= random.choice(animall).lower()
        return final_answer
         
    elif choice == 6 :
        final_answer = random.choice(subjects).lower()
        return final_answer
         
    elif choice == 7 :
        final_answer = random.choice(sports).lower()
        return final_answer
         
    elif choice == 8 :
        final_answer = random.choice(things).lower()
        return final_answer
        
    elif choice == 9 :
        final_answer = random.choice(vegtebale).lower()
        return final_answer
         
    elif choice == 10 :
        final_answer = random.choice(nature).lower()
        return final_answer
        
    else :
        final_answer = random.choice(places).lower()
        return final_answer
         

    
def game_run():

    #call the welcome function to get the game running
    welcome()
    
    #Define a variable alpahabet
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    
    #Set guess word to get_word function for a random word to be generated
    word = get_word()
    
    #Initiate an empty list for guessed letter
    letters_guessed = []
    wrong_guessed = []
    
    #Initiate a tries variable for number of tries by the user
    tries = len(word) + 2 
    
    #Set inital guess to false
    guessed = False
    
    #Print an empty line
    print()
    
    #Print a guess hint for the user for number of letters contained in the word

    print('\033[35mThe word contains '+ str(len(word))+' letters.\033[0m')
    print(len(word) * ' _ ')
    
    #Initate a while loop and create decisions, taking into consideration if the user decides to enter just a single letter or  the full word
    #Also a create decisions for if user inputs a wrong entry and if user inputs letters and it is not equal to the total number of letters in the word to guess
    #Deduct tries each user fails to guess incorrectly
    while guessed == False and tries > 0:

        print('\n\033[47mYou have ' + str(tries) + ' tries\033[49m')
        guess = input('Guess a letter in the word or enter the full word: ').lower()
        #user inputs a letter
        if len(guess) == 1:
            if guess not in alphabet:
                print('\033[33m You are yet to enter a letter. Check your entry, make sure you enter an alphabet not a number\033[0m')

            elif guess in letters_guessed:
                print('\033[31m You have already guessed that letter before.Try again! \033[0m')

            elif guess not in word:
                print('\033[31m Sorry, that letter is not part of the word :( \033[0m')
                wrong_guessed.append(guess)
                letters_guessed.append(guess)
                # print a list of wrong guessed
                print (wrong_guessed)

                tries -=1
            elif guess in word:
                print('Great! That letter exists in the word!')
                letters_guessed.append(guess)

            else:
                print('Check your entry!You might have entered the wrong entry')

        #user inputs the full word
        elif len(guess) == len(word):
            if guess == word:
                print('\033[32mGreat Job! You guessed the word correctly!\033[0m')
                guessed = True
            else:
                print('\033[31mSorry, that was not the word we were looking for :( \033[0m')
                tries -= 1

        #user inputs letters and it is not equal to the total number of letters in the word to guess.  
        else:
            print('\033[31mThe length of your guess is not the same as the length of the correct word.\033[0m')
            tries -=1

        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += ' _ '
            print(status)
           

        if status == word:
            print('\033[32mGreat Job! You guessed the word correctly!\033[0m')
            guessed = True
        elif tries == 0:
            print("\033[31mOpps! You ran out of guesses and you couldn't guessed the word.\033[1m")

     #Initiate play_again function if user wishes to continue
    play_again()

#Full program run
game_run()

