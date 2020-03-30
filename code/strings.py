#strings in Python are arrays of bytes representing unicode characters.
#Python does not have a character data type, a single character is simply a string with a length of 1.

#Note: All string methods returns new values. They do not change the original string.

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