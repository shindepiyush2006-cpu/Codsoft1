import random
import string

print("!! Password Generator !!")

length = int(input("Enter the desired password length: "))
if int(length) == 0: 
 print("sorry can't generate password" )
else:

 characters = string.ascii_letters + string.digits

 password = ''.join(random.choice(characters) for i in range(length))

 print("\nYour Generated Password is:", password)
print("Thank you!!")
