# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
 # Create tuple
fruits_ya = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
# fruits2_ya = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2_ya = ('Apples',)

# Get value
print(fruits_ya[1])

# Can't change value
fruits_ya[0] = 'Pears'

# Delete tuple
del fruits2_ya

# Get length
print(len(fruits_ya))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set_ya = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set_ya)

# Add to set
fruits_set_ya.add('Grape')

# Remove from set
fruits_set_ya.remove('Grape')

# Add duplicate
fruits_set_ya.add('Apples')

# Clear set
fruits_set_ya.clear()

# Delete
del fruits_set_ya

print(fruits_set_ya)