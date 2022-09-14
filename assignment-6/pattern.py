from pyfiglet import Figlet

f = Figlet(font='standard')
print(f.renderText('ّamirala'))


def pattern (m , n):

    row = m 
    col = n 

    for i in range (1 ,row+1):
        
            if (i % 2 ==  0 ):
                if ( col % 2 == 0 ):

                    QTY1= m // 2
                    output = "$&"  * QTY1
                    print (output)

                else :
                    QTY2=(m // 2)+1
                    output = "$&"  * QTY2
                    print (output[:-1])

        
            else :
                if ( col % 2 == 0 ):

                    QTY3= m //2 
                    output1 = "&$"  * QTY3
                    print (output1)

                else :
                    QTY4=(m//2)+1
                    output1 = "&$"  * QTY4
                    print (output1[:-1])
                    
    print(' ')
        

        
        

    # if n % 2 ==0 :
    #     gap = n // 2 
    # else :
    #     gap =( n // 2)+1

    # for i in reversed(range(row)):
    #     for j in reversed(range(col)):
         
        


m = int (input("plz enter your desier number for row:"))
n  = int (input("plz enter your desier number for column:"))
pattern(m , n)