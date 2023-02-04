# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers_ya = [1, 2, 3, 4, 5]
fruits_ya = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2_ya = list((1, 2, 3, 4, 5))

# Get a value
print(fruits_ya[1])

# Get the last value
print(fruits_ya[-1])



# Get length
print(len(fruits_ya))

# Append to list
fruits_ya.append('Mangos')

# Remove from list
fruits_ya.remove('Grapes')

# Insert into position
fruits_ya.insert(2, 'Strawberries')

# Change value
fruits_ya[0] = 'Blueberries'

# Remove with pop
fruits_ya.pop(2)

# Reverse list
fruits_ya.reverse()

# Sort list
fruits_ya.sort()

# Reverse sort
fruits_ya.sort(reverse=True)

print(fruits_ya)