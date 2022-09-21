

from unittest import result

from termcolor import  cprint

cprint ("In  this program if you enter n we send you n+nn+nn -2- -> -246- " , 'red')
num = int (input("Enter a number please : "))

num1 = num * 2 
num2 = num * 3 

cprint( str(num)+str(num1)+str(num2) , 'magenta')
