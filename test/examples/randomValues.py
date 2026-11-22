import random


for i in range(3):
  print(random.random())


for i in range(3):
  print(random.randint(10, 30))


members = ['john', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)

print(leader)