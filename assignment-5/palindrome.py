from termcolor import colored

text= colored('\n\t\033[1m' + 'This program is about palindrome' + '\033[1m \n' ,
                 attrs=['blink','bold'])
print (text )


string = input(colored('Enter a text: ' , 'yellow'))
if string == string[::-1]:
    print(colored('Palindrome' , 'green'))
else:
    print(colored('Not Palindrome' , 'red'))
