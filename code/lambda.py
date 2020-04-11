# A lambda function is a small anonymous function. (normal def functions have names)
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression, The expression is executed and the result is returned
x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#lambda vs def:
def cube(y):
    return y*y*y
    
print(cube(5))

g = lambda x: x*x*x  #no return keyword needed
print(g(7)) 
  


# The power of lambda is better shown when you use them as an anonymous function
#  inside another function.
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) #22
print(mytripler(11)) #33

# filter() with lambda
# The filter() function in Python takes in a function and a list as arguments.

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print("filer:",final_list) #[5, 7, 97, 77, 23, 73, 61]

final_list = list(map(lambda x: x*2 , li)) 
print("map:",final_list) #[10, 14, 44, 194, 108, 124, 154, 46, 146, 122]

# from functools import reduce
# li = [5, 8, 10, 20, 50, 100] 
# sum = reduce((lambda x, y: x + y), li) 
# print ("reduce",sum)