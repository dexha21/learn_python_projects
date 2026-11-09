#Remove duplicates from a list
#my solution

char = [1, 2, 4, "a", "e", "a", 2, 1, 1]

for c in char:
  existed = char.count(c)
  if existed > 1:
    for x in range(existed-1):
      char.remove(c)
      
    print(f"{c} removed {existed-1} times")
    
print(char)

#Mosh
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers:
  if number not in uniques:
    uniques.append(number)
print(uniques)