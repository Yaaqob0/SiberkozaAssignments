# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile_ya = open('myfile_ya.txt', 'w')

# Get some info
print('Name: ', myFile_ya.name)
print('Is Closed : ', myFile_ya.closed)
print('Opening Mode: ', myFile_ya.mode)

# Write to file
myFile_ya.write('I love Python')
myFile_ya.write(' and JavaScript')
myFile_ya.close()

# Append to file
myFile_ya = open('myfile_ya.txt', 'a')
myFile_ya.write(' I also like PHP')
myFile_ya.close()

# Read from file
myFile_ya = open('myfile_ya.txt', 'r+')
text_ya = myFile_ya.read(100)
print(text_ya)