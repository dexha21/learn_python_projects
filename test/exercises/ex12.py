#find the largest number in a list

largest_num = 0
index_pos = 0

numbers = ['Strings', 3, 6, 10, 100.5, 9, 200, 255, -1, 'A']
i = 0


for x in numbers:
  if type(x).__name__ == 'int' or type(x).__name__ == 'float' :
    if x > largest_num:
      largest_num = x
      index_pos = i
  else:
    print(f"{numbers[i]} is not a valid number")
  
    
  i += 1

print(f"The largest number on the list is {largest_num}")