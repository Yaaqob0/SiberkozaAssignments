# If/ Else conditions are used to decide to do something based on something being true or false

x_ya = 21
y_ya = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x_ya > y_ya:
  print(f'{x_ya} is greater than {y_ya}')

# If/else
if x_ya > y_ya:
  print(f'{x_ya} is greater than {y_ya}')
else:
  print(f'{y_ya} is greater than {x_ya}')  

# elif
if x_ya > y_ya:
  print(f'{x_ya} is greater than {y_ya}')
elif x_ya == y_ya:
  print(f'{x_ya} is equal to {y_ya}')  
else:
  print(f'{y_ya} is greater than {x_ya}')  

# Nested if
if x_ya > 2:
  if x_ya <= 10:
    print(f'{x_ya} is greater than 2 and less than or equal to 10')
    

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x_ya > 2 and x_ya <= 10:
    print(f'{x_ya} is greater than 2 and less than or equal to 10')

# or
if x_ya > 2 or x_ya <= 10:
    print(f'{x_ya} is greater than 2 or less than or equal to 10')

# not
if not(x_ya == y_ya):
  print(f'{x_ya} is not equal to {y_ya}')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

#  in
if x_ya in numbers:
  print(x_ya in numbers)

# not in
if x_ya not in numbers:
  print(x_ya not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x_ya is y_ya:
  print(x_ya is y_ya)

# is not
if x_ya is not y_ya:
  print(x_ya is not y_ya)