import random

def guess(x):
  rand_num = random.randint(1, x)
  
  val = 0
  trial = 0
  while val != rand_num:
    try:
      val = int(input(f"Guess a number between 1 and {x}: "))
    except ValueError:
      print("Numbers only. Game restarted with same difficulty")
      guess(x)
    trial += 1
    if val > rand_num:
      print("Too high! Try again.")
    if val < rand_num:
      print("Too low! Try again.")
  print(f"You have guessed the number {rand_num} correctly with {trial} {"tries" if trial > 1 else "try"}")


#game difficulty
status = True
diff = ""

while status:
  diff = input("Please enter difficulty (e for easy, m for medium, h for hard, x for extremely hard): ").lower()
  match diff:
    case "e":
      guess(100)
      status = False
    case "m":
      guess(1000)
      status = False
    case "h":
      guess(10000)
      status = False
    case "x":
      guess(1000000)
      status = False
    case _:
      print("Invalid selection. Try again.")