primary_colors = set(["red", "blue", "yellow"])

color = "green"

if color in primary_colors:
  print(color + " is in the set.")
else:
  print(color + " is not in the set.")

letters = set(["a", "b"])
letters.add("c")
print(letters)