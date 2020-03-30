
# Python is an interpreted programming language.
# Python relies on indentation, using whitespace, to define scope;
# such as the scope of loops, functions and classes.
# Other programming languages often use curly-brackets for this purpose.

# comments,variables,datatypes,tyepcasting

print("Hello, World!")
print("Hello:",5)
print("Hello: {}".format(5))
print("Hello: {0:.2f}, {1:.2f},{2:.3f}".format(5.5648,5.5658,5.5698)) #5.56, 5.57, 5.570

x = 5
print(type(x)) #int //unlimited length.

x = 5.0 #float
z = 3+1j # complex

y = "John"  #str
y = 'John'
print("Hello:"+y) #+ can only concatenate str (not "int") to str

y = True #bool
y = False
x = b"Hello" #bytes
x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"
x = ["apple", "banana", "cherry"] #list
x = ("apple", "banana", "cherry") #tuple
x = {"apple", "banana", "cherry"} #set
x = frozenset({"apple", "banana", "cherry"}) #frozenset
x = {"name" : "John", "age" : 36} #dict

#If you want to specify the data type, you can use the following constructor functions:
x = str("Hello World")
z = str(3.0)  # z will be '3.0'
x = int(20)
x = list(("apple", "banana", "cherry"))
x = float(1)     # x will be 1.0
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

def firstProgram(msg):
    print('Hello Deepak',msg)

firstProgram("Good morning")

import random

print("random no: ",random.randrange(1,10))

#python variable names are case-sensitive
#Variables that are created outside of a function are known as global variables.
#To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

#Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3 #35000.0
y = 12E4 #120000.0
z = -87.7e100  #-8.77e+101

#Python does not really have a syntax for multi line comments.
#Since Python will ignore string literals that are not assigned to a variable, 
# you can add a multiline string (triple single or double quotes) in your code, and place your comment inside it:

'''
This is a comment
written in
more than just one line
'''

s='''This is a 
multiline string'''