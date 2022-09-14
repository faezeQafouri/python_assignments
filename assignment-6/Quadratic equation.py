import math


def delta (a , b , c ):
    #delta = b^2 - 4ac 
    delta = (b ** 2) - (4 * a * c)
    return delta


a = int(input("enter A:"))
b = int(input("enter B:"))
c = int(input("enter C:"))

Δ = delta(a , b , c)

if Δ < 0 :
    print ("We dont have any answer for Δ<0 !!!!")


elif Δ == 0 :
    ans = (-1 * b )/ a
    print ("Δ = 0  \nThe answer to the equation is equal to : ",ans)


elif Δ > 0 :

    x1 = ((-1 * b) - math.sqrt(Δ)) / (2 * a)
    x2 = ((-1 * b) + math.sqrt(Δ)) / (2 * a)
    print ("Δ > 0  \nThe answers to the equation is equal to :")
    print ("ans1:" , x1)
    print ("ans1:" , x2)