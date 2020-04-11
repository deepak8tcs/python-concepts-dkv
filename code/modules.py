# Module(library) is a python file containing a set of functions.
# To create a module just save the code you want in a file with the file extension .py.


# Using a module:
# by using the import statement:
  
import basics #prints everything from basics
#import basics as b   #renaming,alias
basics.firstProgram("Good morning") 
print(basics.x)

  
from basics import firstProgram #You can choose to import only parts from a module
firstProgram("Good morning") 

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like
import platform

x = platform.system()
print(x) #Windows

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module.
# Note: The dir() function can be used on all modules, also the ones you create yourself.
x = dir(platform)

#['DEV_NULL', '_UNIXCONFDIR', '__cached__', '__copyright__', 'system','version', 'warnings', 'win32_ver']