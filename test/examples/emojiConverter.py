message = input("> ")

words = message.split(" ")

emojis = {
  ":)": "**smiling**",
  ":(": "**sad**",
  ":-(": "**angry**"
}

output = ""

for word in words:
  output += emojis.get(word, word) + " "

print(output)