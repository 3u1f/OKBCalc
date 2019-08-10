import math

num1 = round(15000) 
num2 = round(30000)
num3 = round(45000)
num4 = round(60000)
num5 = round(75000)
num0 = int(input("Enter the number of days left 1-30:"))

print("Coefficent 1 =",math.ceil(num1/num0),"OKB")
print("Coefficent 2 =",math.ceil(num2/num0),"OKB")
print("Coefficent 3 =",math.ceil(num3/num0),"OKB")
print("Coefficent 4 =",math.ceil(num4/num0),"OKB")
print("Coefficent 5 =",math.ceil(num5/num0),"OKB+")