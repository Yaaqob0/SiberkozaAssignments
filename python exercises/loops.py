# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_ya = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people_ya:
  print(f'Current Person: {person}')

# Break
for person in people_ya:
  if person == 'Sara':
    break
  print(f'Current Person: {person}')

# Continue
for person in people_ya:
  if person == 'Sara':
    continue
  print(f'Current Person: {person}')

# range
for i in range(len(people_ya)):
  print(people_ya[i])

for i in range(0, 11):
  print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count_ya = 0
while count_ya < 10:
  print(f'Count: {count_ya}')
  count_ya += 1