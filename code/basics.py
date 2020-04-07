
# Python is an interpreted programming language.
# Python relies on indentation, using whitespace, to define scope;
# such as the scope of loops, functions and classes.
# Other programming languages often use curly-brackets for this purpose.

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
