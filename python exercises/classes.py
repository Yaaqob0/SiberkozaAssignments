# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User_ya:

  # Constructor
  def __init__(self, name_ya, email_ya, age_ya):
    self.name_ya = name_ya
    self.email_ya = email_ya
    self.age_ya = age_ya
    
    # Adding Encapsulation of variables... Encapsulation is the concept of making the variables non-accessible or accessible upto some extent from the child classes
    self._private = 1000 # Encapsulated variables are declares with '_' in the constructor.

  def greeting(self):
      return f'My name is {self.name_ya} and I am {self.age_ya}'

  def has_birthday(self):
      self.age_ya += 1
 
 #function for encap variable
  def print_encap(self):
      print(self._private)

# Extend class
class Customer(User_ya):
  # Constructor
  def __init__(self, name_ya, email_ya, age_ya):
      User_ya.__init__(self, name_ya, email_ya, age_ya) #Called proper parent class constructor to make this as proper child inehriting all methods.
      self.name_ya = name_ya
      self.email_ya = email_ya
      self.age_ya = age_ya
      self.balance = 0

  def set_balance(self, balance):
      self.balance = balance

  def greeting(self):
      return f'My name_ya is {self.name_ya} and I am {self.age_ya} and my balance is {self.balance}'

#  Init user object
brad_ya = User_ya('Brad_ya Traversy', 'brad_ya@gmail.com', 37)
# Init customer object
janet_ya = Customer('Janet_ya Johnson', 'janet_ya@yahoo.com', 25)

janet_ya.set_balance(500)
print(janet_ya.greeting())

brad_ya.has_birthday()
print(brad_ya.greeting())

#Encapsulation -->
brad_ya.print_encap()
brad_ya._private = 800 #Changing for brad_ya
brad_ya.print_encap()

# Method inherited from parent
janet_ya.print_encap() #Changing the variable for brad_ya doesn't affect janet_yas variable --> Encapsulation
janet_ya._private = 600
janet_ya.print_encap()

#Similary changing janet_ya's doesn't affect brad_ya's variable.
brad_ya.print_encap()