print("You can choose the opearations by entering following numbers\n")
print("1 - ADD")
print("2 - SUBSTRACTION")
print("3 - MULTIPLICATION")
print("4 - DIVISION\n")
option = int(input("Choose an Operation:"))
if (option in [1, 2, 3, 4]):
  print("\nSure Sir!!")

  num1 = int(input("Enter first number:"))
  num2 = int(input("\nEnter second number:"))
  if (option == 1):
    result = num1 + num2
  elif (option == 2):
    result = num1 - num2
  elif (option == 3):
    result = num1 * num2
  elif (option == 4):
    result = num1 / num2
    
else :
    print("Invalid Operation") 
  
print("\nThe result of the operation is {}".format(result))
