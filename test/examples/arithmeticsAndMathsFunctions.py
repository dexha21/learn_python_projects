#Arithmetics in python
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3) #integer return only
print(10 % 3) #module (what remains from a division)
print(10 ** 3) #power (raise to power)


x = 10

x -= 3 #still the same as x = x - 3

print(x)

##operator precedence
#parenthesis > exponentiation (**) > multiplication or division > addition or subtraction

x = 10 + 3 * 2 ** 2 / (5 + 4)

print(x)



#math functions
x = 2.9
print(round(x)) #round

print(abs(-2.9)) #absolute always return a positive number

