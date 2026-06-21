import sys
print("Enter Your Age : ")
age = input()

#Print Data Type
print(type(age))

#Print Memory Address
print(id(age))

#Print Size in bytes
print(sys.getsizeof(age))