# try: block lets you test a block of code for errors.
# except: block lets you handle the error.
# finally: block lets you execute code, regardless of the result of the try- and except blocks.
# raise: To throw(raise) an exception if a condition occurs.
# else: to define a block of code to be executed if no errors were raised: 

try:
  print(x)
except NameError:
  print("Variable x is not defined. error name:",NameError.__name__)
except:
  print("Something else went wrong")
finally:
  print("The 'try except' is finished") 

#else:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
#--------------------------------
try:
  print(x)
except Exception:
  print("Something else went wrong:",Exception.__name__)  

#raise:
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
#You can define what kind of error to raise, and the text to print to the user.
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")