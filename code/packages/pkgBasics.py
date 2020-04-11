
# A package is basically a directory with Python files and a file with the name __init__.py.
# This means that every directory inside of the Python path, which contains a file named __init__.py, 
# will be treated as a package by Python. It's possible to put several modules into a Package.

#A package is imported like a "normal" module.

from packageA import a, b
a.bar()
b.foo()



# __init__.py file can be empty, or it can contain valid Python code. 
# This code will be executed when a package will be imported, 
# so it can be used to initialize a package, 
# e.g. to make sure that some other modules are imported or some values set.

# we can't access neither "a" nor "b" by solely importing packageA.
# Yet, there is a way to automatically load these modules. 
# We can use the file __init__.py for this purpose.
#  All we have to do is add the following lines to the so far empty file __init__.py:
# import simple_package.a
# import simple_package.b

import packageA
packageA.a.bar()
packageA.b.foo()

from packageA import *
a.bar()
b.foo()

print(dir(packageA))
#['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'a', 'b', 'packageA']