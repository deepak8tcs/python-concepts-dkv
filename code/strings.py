#strings in Python are arrays of bytes representing unicode characters.
#Python does not have a character data type, a single character is simply a string with a length of 1.
#Note: All string methods returns new values. They do not change the original string.

# String is immutable in python as well like in java. 
# In fact, Integers, Floats, and Tuples are also immutable data types in python. 
# List, sets, dictionary are mutable data types. Also, there are no primitives in python. 
# Everything is an object


a = "Hello, World!" #left to right index 0,1,2.... right to left: -1,-2,3
print(a[1])
print(a[2:5]) # llo #return range-slicing syntax:2 included ,5 is not. separated by colon.
print(a[-5:-2]) #orl #value is printed from -5 to -3
print(len(a))
print(a.lower())
print(a.upper())
print(a.capitalize()) #first character to upper case,rest all lower case, Hello, world
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']  //returns a list


a = " Hello, World! "
print(a.strip()) #The strip() method removes any whitespace from the beginning or the end:

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple") #2
x = txt.count("apple", 10, 24) #1

print("endsWith:",txt.endswith("fruit")) #starts/endswith,contains: True/False
print(txt.startswith("I"))
x = "ain" in txt #contains, not contains: True/False
x = "ain" not in txt

#Membership operators(in, not in) are used to test if a sequence is presented in an object:
x = ["apple", "banana"]
print("banana" in x) #True

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x) #John#Peter#Vicky


print(a+" "+txt) #string concat with + operator

#print("hi"+5) #string and number cannnot be combined with +, we can use format to insert no. into string
print("hi {}".format(5))
#The format() method takes unlimited number of arguments, and are placed into the respective placeholders
print("Hello: {},{},{}".format(5,6,7)) #5,6,7
print("Hello: {2},{0},{1}".format(5,6,7)) #7,5,6
print("My name is {fname}, I'am {age}".format(fname = "Deepak", age = 30))


#To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash \ followed by the character you want to insert.
txt = "We are the so-called \"Vikings\" from the north." # "Vikings"
txt = "We are the so-called \\Vikings\\ from the north." # \Vikings\

print('you\'ll have success here')
#or
print("you'll have success here")
# ******Python String Comparison
# Python string comparison is performed using the characters in both strings. 
# The characters in both strings are compared one by one.
# When different characters are found then their Unicode value is compared. 
# The character with lower Unicode value is considered to be smaller.

print('A unicode is', ord('A'), ',a unicode is', ord('a')) #a=97, A=65
print('apple' == 'Apple') #False
print('apple' > 'Apple') #True
print('Apple' < 'ApplePie') #True
# If the characters sequence are the same in both the strings but one of them have some additional
#  characters, then the larger length string is considered greater than the other one.

print('string comparison:')
print('Banana' == 'Apple') #False
print('Banana' < 'Apple') #False
print('Banana' > 'Apple') #True

# banana comes after apple in the dictionary.
fruit1 = input('Please enter the name of first fruit:\n') #banana
fruit2 = input('Please enter the name of second fruit:\n') #apple

if fruit1 < fruit2:
    print(fruit1 + " comes before " + fruit2 + " in the dictionary.")
elif fruit1 > fruit2:
    print(fruit1 + " comes after " + fruit2 + " in the dictionary.")
else:
    print(fruit1 + " and " + fruit2 + " are same.")


# *******************************
#String is immutable in python as well like in java. Immutable objects are thread safe.
name="python"
#name[0]='z' #we cannot change the original string here to zython
#above shows error "name doesnt support item assignment"

s1="hi"
s2="hi"
print(id(s1),id(s2)) #same memory locations:15114688 15114688, memory allocation only once
s1=s1+s2
print(id(s1),id(s2)) #memory locations:14040064 15114688

myList = [1 , 2 , 3]
print(id(myList))      #This will print id like 9656360.
myList.append(5)       #This appends 5 to the list resulting in
                       # myList to be[1, 2, 3, 5]
print(id(myList))      #This will print id with the same value as
                       # before 9656360.


# Method	True if
# str.isalpha()	String consists of only alphabetic characters (no symbols)
# str.isnumeric()	String consists of only numeric characters
# str.isalnum()	String consists of only alphanumeric characters (no symbols)
# str.isspace()	String consists of only whitespace characters
# str.istitle()	String is in title case
# str.isupper()	String’s alphabetic characters are all upper case
# str.islower()	String’s alphabetic characters are all lower case