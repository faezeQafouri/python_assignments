
import sys
import pyfiglet
from termcolor import  cprint
from colorama import Fore,Back, init

init()

def multiple_table (row , col):

    pattern = [ [i*j  for i in range (1 , row+1)]  for j in range (1 , col+1) ]


    for i in range (row):
        
        for j in range (col):
            cprint(pattern[i][j] ,'yellow' ,end= '\t')
            
        print(' ')
            

row = int (input (Fore.YELLOW +"enter your desire row number : " ) )  

col = int (input (Fore.YELLOW + "enter your desire row number :")  )

multiple_table(row , col)
