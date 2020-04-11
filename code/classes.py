# Python Classes/Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.

class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

# All classes have an in-built function called __init__(), which is always
# executed when the class is being initiated/instanciated.
# Use the __init__() function to assign values to object properties

# The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.
# It does not have to be named self , you can call it whatever you like,
#  but it has to be the first parameter of any function in the class:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.myfunc()
p1.age = 40 #modify value
del p1.age #delete object property
del p1 #delete object

class Person1:
  pass

# class definitions cannot be empty, but if you for some reason have a class
# definition with no content,put in the pass statement to avoid getting an error.

#*****INHERITANCE****************************************

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.myfunc()

# The child's __init__() function overrides the inheritance of the parent's __init__() function.
# Python also has a super() function that will make the child class inherit 
# all the methods and properties from its parent:
class Person2:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
  def welcome(self):
    print("welcome parent:",self.firstname, self.lastname)

class Student1(Person2):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)   #   Person.__init__(self, fname, lname) or
        self.graduationyear = year
        self.college = 'BBD'
 
    def welcome(self): #method overriding
       print("Welcome student ", self.firstname, self.lastname, "to the class of", self.graduationyear)  
          
s = Student1("Mike", "Olsen", 2011)
s.welcome() 
s.printname()