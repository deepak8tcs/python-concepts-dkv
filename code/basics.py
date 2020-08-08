#Python is an interpreted, high-level, general-purpose programming language.
#It is is dynamically typed and garbage-collected.

# Python relies on indentation, using whitespace, to define scope;
# such as the scope of loops, functions and classes.
# Other programming languages often use curly-brackets for this purpose.

#For the most part, Python is an interpreted language and not a compiled one, 
#although compilation is a step. Python code, written in .py file is first compiled
#to what is called bytecode which is stored with a .pyc or .pyo format.

# comments,variables,datatypes,tyepcasting

import random
print("Hello, World!")
print("Hello:",5) #will print them out separately, with a space.
print("Hello: {}".format(5))
print("Hello: {0:.2f}, {1:.2f},{2:.3f}".format(
    5.5648, 5.5658, 5.5698))  # 5.56, 5.57, 5.570

x = 5
print(type(x))  # int //unlimited length.

x = 5.0  # float
z = 3+1j  # complex

y = "John"  # str
y = 'John'
print("Hello:"+y)  # + can only concatenate str (not "int") to str

y = True  # bool
y = False
x = b"Hello"  # bytes
x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # tuple is immutable,written with round brackets.
x = {"apple", "banana", "cherry"}  # set
x = frozenset({"apple", "banana", "cherry"})  # frozenset
x = {"name": "John", "age": 36}  # dict

# If you want to specify the data type, you can use the following constructor functions:
x = str("Hello World")
z = str(3.0)  # z will be '3.0'
x = int(20)
x = list(("apple", "banana", "cherry"))
x = float(1)     # x will be 1.0
z = float("3")   # z will be 3.0
w = float("4.2")  # w will be 4.2

print(bool("Hello"))
print(bool(15))
print(bool(["apple", "cherry", "banana"]))
print("allFalse:", bool(""), bool(0), bool([]))  # allFalse
print("None is:", bool(None))  # allFalse

# Most Values are True
# empty string, empty iterable, number 0, None are False.
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# Logical operators java vs python": &&=>and, ||=>or, !=>not
print("Logical operators:", not(True and True or False))  # False
print("Logical operators:", not(True and False or False))  # True

# Identity operators (is,is not)are used to compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location:
# is/is not compares content & memory location both,but "==" compares only content
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)  # returns True because z is the same object as x
# returns False because x is not the same object as y, even if they have the same content
print(x is y)
print(x == y)  # True

print(None == None)  # True
print(None is None)  # True



def firstProgram(msg):
    print('Hello Deepak', msg)


firstProgram("Good morning")


print("random no: ", random.randrange(1, 10))

# python variable names are case-sensitive
# Variables that are created outside of a function are known as global variables.
# To create a global variable inside a function, you can use the global keyword.


def myfunc():
    global x
    x = "fantastic"


# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3  # 35000.0
y = 12E4  # 120000.0
z = -87.7e100  # -8.77e+101

# Python does not really have a syntax for multi line comments.
# Since Python will ignore string literals that are not assigned to a variable,
# you can add a multiline string (triple single or double quotes) in your code, and place your comment inside it:

'''
This is a comment
written in
more than just one line
'''

s = '''This is a 
multiline string'''

# Python has two primitive loop commands:
# while loops
# for loops
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#  Note: remember to increment i, or else the loop will continue forever. 
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
else:
  print("i is no longer less than 6")  


# if, elif, else. Notice elif keyword.

#loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break  

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and ends at a specified number.

for x in range(6): #values from 0 to 6 (but not including 6):
  print(x) #6 values: 0,1,2,3,4,5

for x in range(2, 6): #values from 2 to 6 (but not including 6):
  print(x)  

for x in range(2, 30, 3): #Increment the sequence by 3 
  print(x)
else: #executed when the loop is finished.
  print("Finally finished!")

#Nested loop:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass #also used with function,class,except block

# for loops cannot be empty, but if you for some reason have a for loop with no content, 
# put in the pass statement to avoid getting an error.

# Lists, tuples, dictionaries, strings and sets are all iterable objects.
# All these objects have a iter() method which is used to get an iterator:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Global Scope
# A variable created in the main body of the Python code is a global variable
#  and belongs to the global scope.
def myfunc():
  global x #to define a global variable inside local scope we use global keyword
  x = 300

myfunc()

print(x)
