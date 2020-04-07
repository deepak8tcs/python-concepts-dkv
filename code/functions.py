# A function is a block of code which only runs when it is called.
#You can send any data types of argument to a function (string, number, list, dictionary etc.)


def my_function():
  print("Hello from a function")
  return "return example"

my_function()

# Arbitrary Arguments, shortened as *args in Python documentations.
# If you do not know how many arguments that will be passed into your function, 
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function1(*kids):
  print("The youngest child is " + kids[2])

my_function1("Emil", "Tobias", "Linus")


# Keyword Arguments,shortened as kwargs
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.


def my_function2(child3, child2, child1):
  print("The youngest child is " + child3)

my_function2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_function3(**kid):
  print("His last name is " + kid["lname"])

my_function3(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
# If we call the function without argument, it uses the default value:
def my_function4(country = "Norway"):
  print("I am from " + country)

my_function4("India")
my_function4()

# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition
#  with no content, put in the pass statement to avoid getting an error.

def myfunction():
    pass

#Recursion: Python also accepts function recursion, which means a defined function can call itself.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# Recursion Example Results
# 1
# 3
# 6
# 10
# 15
# 21