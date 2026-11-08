numbers = [5, 2, 5, 2, 2]

#solution 1
# for n in numbers:
#   print("x" * int(n))

for n in numbers:
  temp_mem = ""
  for d in range(n):
    temp_mem += "x"
  print(temp_mem)