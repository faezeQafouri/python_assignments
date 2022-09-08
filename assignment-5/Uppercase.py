from termcolor import colored

text= colored('\033[1m' + '---------- about uppercase letters ----------' + '\033[0m' ,
                 attrs=['reverse', 'blink'])
print (text )

names =[]
for i in range (1 , 11):
    name = input("Enter a name "+str(i)+": ")
    
    names.append(name)

print(colored('At first:','yellow'))
print (names)
    
# ma to list upper , title , captalize ndrim az in method estefade mishe to list 
upperscase=[word.title() for word in names]
print(colored('After changing:','green'))
print (upperscase)
