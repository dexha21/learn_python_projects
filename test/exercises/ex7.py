#my solution
name = input("Enter your name: ")

nameLength = len(name)

if nameLength < 3:
  print("name must be at least 3 characters")
elif nameLength > 50:
  print('name can be a maximum of 50 characters')
else:
  print('name looks good!')


#Mash solution

name = ""

if len(name) < 3:
  print("Name must be at least 3 characters")
elif len(name) > 50:
  print("Name must be a maximum of 50 characters")
else:
  print("Name looks good!")