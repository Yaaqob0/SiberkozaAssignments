# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict
person_ya = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
# person2_ya = dict(first_name='Sara', last_name='Williams')

# Get value
print(person_ya['first_name'])
print(person_ya.get('last_name'))

# Add key/value
person_ya['phone'] = '555-555-5555'

# Get dict keys
print(person_ya.keys())

# Get dict items
print(person_ya.items())

# Copy dict
person2_ya = person_ya.copy()
person2_ya['city'] = 'Boston'

# Remove item
del(person_ya['age'])
person_ya.pop('phone')

# Clear
person_ya.clear()

# Get length
print(len(person2_ya))

# List of dict
people_ya = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people_ya[1]['name'])