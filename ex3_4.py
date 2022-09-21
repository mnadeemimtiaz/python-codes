yr_num = int(input('Enter the year:'))

if (yr_num%4 == 0) or (yr_num%100!= 0 and yr_num%400 == 0): #Using Modulus to solve Ref :https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp
    print("This is a leap year")
else:
    print("This is not a leap year")