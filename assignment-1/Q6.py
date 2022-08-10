#q6 -----> about The sum of the second and fifth digits
num = int(input("plz enter a number you want: "))
number_two = ((num// 10) % 10)
number_five = ((num // 10000) % 10)
sum = (number_two + number_five)
print("The sum of the second and fifth digits is=",sum)