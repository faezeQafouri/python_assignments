#q5 ----->  about cylinder 
r = int (input ("plz enter radius of Cylinder : "))
h  = int (input ("plz enter Height of Cylinder : "))
#s=2*pi*r*h
sideArea= 2 * r * 3.14 * h 
# v = pi*r*r*h
v = 3.14 * r * r * h
#total S = 2*pi*r*r + 2*pi*r*h
totalArea = 2 * 3.14 * r * r + 2 * 3.14 * r * h 

print ("Side Area:", sideArea)
print ("cylinder volume:", v)
print ("Total Area:", totalArea)
