seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

for i, row in enumerate(seating_chart):
  for j, student in enumerate(row):
    print(f'row: {i+1}, seat: {j}, student: {student}')
