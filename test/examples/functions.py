def greet_user(first_name, last_name): 
  print(f"Hi {first_name} {last_name}!")
  print("Welcome aboard")
  


greet_user("John", "Smith") #positional  argument
greet_user(last_name="Smith", first_name="John") #keyword argument


def square(number):
  return number * number

print(square(3))