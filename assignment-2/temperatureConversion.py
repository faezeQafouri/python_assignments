
#this program is  conversion f->c or c->f  c->k or k->c  or f->k or k->f:  
while True:

    temp1 = input("Enter the temperature unit you need:" )
    temp2 = input("Enter the temperature unit you need for convert:" )

#convert celcious to farehnhite
    if temp1 == "celsius" and temp2 == "fahrenheit" :
         celsius = float(input("Enter temperature in celsius: "))
         fahrenheit = (celsius * 9/5) + 32
         print( " %.2f Celsius is: %0.2f Fahrenheit" %(celsius, fahrenheit))

#convert celcious to kelvin
    elif temp1 == "celsius" and temp2 == "kelvin" :
         celsius = float(input("Enter temperature in celsius: "))
         kelvin = 273.15 + celsius
         print(" %0.3f Celsius = %0.3f Kelvin." % (celsius, kelvin))


#convert  farehnhite to celsius
    elif temp1 == "fahrenheit" and temp2 == "celsius" :
         fahrenheit = float(input("Enter temperature in fahrenheit: "))
         celsius = (fahrenheit - 32) * 5/9
         print(" %.2f Fahrenheit is: %0.2f Celsius " %(fahrenheit, celsius))

#convert  farehnhite to kelvin 
    elif temp1 == "fahrenheit" and temp2 == "kelvin" :
         fahrenheit = float(input("Enter temperature in fahrenheit: "))
         kelvin = 5 * (fahrenheit-32)/9 + 273.15
         print(" %.2f Fahrenheit is: %0.2f kelvin" %(fahrenheit, kelvin))
    
#convert  kelvin to  farehnhite
    elif temp1 == "kelvin" and temp2 == "fahrenheit":
         kelvin = float(input("Enter temperature in kelvin: "))
         fahrenheit = (1.8 * kelvin)-459.67
         print(" %.2f kelvin is: %0.2f fahrenheit" %(kelvin, fahrenheit))

#convert  kelvin to celcious 
    elif temp1 == "kelvin" and temp2 == "celsius" :
         kelvin = float(input("Enter temperature in kelvin: "))
         celsius =  kelvin- 273.15 
         print("%.2f kelvin is: %0.2f celsius" %(kelvin, celsius))

    else :
        print ("Invalid option !!!! . ")


