#my solution
user_weight = input("Enter Weight: ")

unit = input("(L)bs or (K)g: ")

output = 0

if unit.lower() == "l":
  output = f"You are {round(float(user_weight) * 0.453592, 3)} kilos"
elif unit.lower() == "k":
  output = f"You are {round(float(user_weight) / 0.453592, 3)} pounds"
else:
  output = "Invalid value"

print(output)
