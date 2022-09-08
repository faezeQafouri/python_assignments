
from termcolor import colored , cprint

text= colored('\033[1m' + '----------- about join & split words ----------' + '\033[0m\n' ,
                 attrs=['reverse', 'blink'])
print (text )


def computer_prompt():
    return (colored('Computer: ', 'green' , 'on_green'))
def user_prompt():
    return (colored('User:', 'yellow' , 'on_yellow'))
 
print(computer_prompt()+' Please enter a word or Sentence.')
 
word = input(user_prompt()+' ')

split_word= input(user_prompt()+(" With which string do you want to split the text? :"))

join_word= input(user_prompt()+(" Then, which string do you want to join the text? :"))

if split_word =="":
    li = word.split()

else :
    li = word.split(split_word)


print(colored('resualt for split :\n' ,'green') ,'\t',li)

print (colored('resualt for join :\n' , 'green'),'\t',join_word.join(li))
 
