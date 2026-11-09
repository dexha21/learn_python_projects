num_dic = {
  "0": "Zero",
  "1": "One",
  "2": "Two",
  "3": "Three",
  "4": "Four",
  "5": "Five",
  "6": "Six",
  "7": "Seven",
  "8": "Eight",
  "9": "Nine",
}

user_num = input("Phone: ")

output = ""
for num in user_num:
  output += num_dic.get(num) + ", "

print(output)