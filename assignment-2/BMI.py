import os 
os.system('cls')



while True : 

 height = float(input("plz enter you're height (m):"))
 Weight = float(input("plz enter you're weight (kg):"))

 BMI = Weight / height * height

 if 16 <= BMI < 18.5:
     print("You're BMI is: " , BMI , " You should Gain some weight Asap. ")
     break

 elif  18.5 <= BMI < 24:
     print("You're BMI is " ,BMI, "Congratulations! Your weight is Normal. ")
     break

 elif 24 <= BMI < 30:
    print("You're BMI is " ,BMI , "You're slightly Overweight , keep in Your Diet. ")
    break

 elif 30 <= BMI < 35:
    print("You're BMI is " ,BMI, "You've got first Degree Obesity , You should go on a Diet. ")
    break

 elif 35 <= BMI < 40:
    print("You're BMI is " ,BMI, "You've got second Degree Obesity , You have to go on a Diet , It's almost Dangerous!")
    break

 elif BMI >= 40:
    print("You're BMI is " ,BMI, "You've got third Degree Obesity , You have to go on a Diet , You're Health care is in Danger! ")
    break
 else:
     print("Invalid Information!\bPlz tryagain.")
     continue


