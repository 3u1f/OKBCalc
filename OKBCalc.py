import math

while True:
  
  num1 = 15000
  num2 = 30000
  num3 = 45000
  num4 = 60000
  num5 = 75000
  num6 = 5
  num0 = int(input("Enter the number of days left 1-5:"))
  print("")
  if num0 > 5:
    print("")
    print("Number too high")
    print("")
  else: 
    print("Minimum OKB needed for Coefficent 1 with",(num0),"days left is",math.ceil(num1/num0),"OKB")
    print("")
    print("Minimum OKB needed for Coefficent 2 with",(num0),"days left is",math.ceil(num2/num0),"OKB")
    print("")
    print("Minimum OKB needed for Coefficent 3 with",(num0),"days left is",math.ceil(num3/num0),"OKB")
    print("")
    print("Minimum OKB needed for Coefficent 4 with",(num0),"days left is",math.ceil(num4/num0),"OKB")
    print("")
    print("Minimum OKB needed for Coefficent 5 with",(num0),"days left is",math.ceil(num5/num0),"OKB+") 
    print("")

  answer = "y"
  answer = input("Would you like to run again, type y for yes and n for no: ")
  print("")
  if answer == "y":
    continue    
  else:
    break
