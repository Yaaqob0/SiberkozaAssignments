 # Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_ya = 'Brad'
age_ya = 37

# Concatenate
print('Hello, my name is ' + name_ya + ' and I am ' + str(age_ya))

# String Formatting

# Arguments by position
print('My name is {name_ya} and I am {age_ya}'.format(name_ya=name_ya, age_ya=age_ya))

# F-Strings (3.6+)
print(f'Hello, my name is {name_ya} and I am {age_ya}')

# String Methods

s_ya = 'helloworld'

# Capitalize string
print(s_ya.capitalize())

# Make all uppercase
print(s_ya.upper())

# Make all lower
print(s_ya.lower())

# Swap case
print(s_ya.swapcase())

# Get length
print(len(s_ya))

# Replace
print(s_ya.replace('world', 'everyone'))

# Count
sub_ya = 'h'
print(s_ya.count(sub_ya))

# Starts with
print(s_ya.startswith('hello'))

# Ends with
print(s_ya.endswith('d'))

# Split into a list
print(s_ya.split())

# Find position
print(s_ya.find('r'))

# Is all alphanumeric
print(s_ya.isalnum())

# Is all alphabetic
print(s_ya.isalpha())

# Is all numeric
print(s_ya.isnumeric())