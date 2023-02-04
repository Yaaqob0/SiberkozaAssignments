# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello_ya(name_ya='Sam'):
    print(f'Hello {name_ya}')


# Return values
def getSum(num1_ya, num2_ya):
    total_ya = num1_ya + num2_ya
    return total_ya


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum_ya = lambda num1_ya, num2_ya: num1_ya + num2_ya

print(getSum_ya(10, 3))