first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print(message)

msg = f'{first} [{last}] is a coder'
#f'' is a formatted string

print(msg)

#String methods
course = 'Python for Beginners'


print(len(course)) #string length

print(course.upper())
print(course.lower())
print(course.title())
print(course.find("y"))
print(course.replace("Be", "be"))
print("for" in course)