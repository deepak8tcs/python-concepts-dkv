# There are four collection data types:
# *List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# *Set is a collection which is unordered and unindexed. No duplicate members.
# *Dictionary(key-value pair) is a collection which is unordered, changeable and indexed. No duplicate members.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist)
print(thislist[0])
print(thislist[-1])  # last element
print(thislist[2:5])  # 2 included,5 not included.
print(thislist[:4])  # start with 0
print(thislist[2:])  # go till last element
print(thislist[-4:-1])  # go from -4 till -2
thislist[1] = "blackcurrant" #list is changeable
print(thislist)
print(len(thislist))
print(thislist.count("orange")) #1
print(thislist.index("apple")) #0, only returns the first occurrence of the value.
print(thislist.reverse())#reverse the element order

for x in thislist:
    print(x)
if "apple" in thislist:  # contains: in,not in
    print("Yes, 'apple' is in the fruits list")


# add,update,remove,clear
thislist.append("orange")  # To add an item to the end of the list
thislist.insert(1, "orange")  # To add an item at the specified index
# several ways to Remove
thislist.remove("blackcurrant")

thislist1 = ["apple", "banana", "cherry"]
thislist1.pop() #removes the specified index, (or the last item if index is not specified)
thislist1.pop(1)
print(thislist1)  # ["apple"]

del thislist[0] #del keyword removes the specified index,can also delete the list completely:
print(thislist)
del thislist1
thislist.clear() #empties the list
#print(thislist1) #error, list is deleted

#You cannot copy(create new list with same value) a list simply by typing list2 = list1, 
# because: list2 will only be a reference to list1, and changes made in list1
#  will automatically also be made in list2.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() #mylist will have new memory location with same content
#mylist2 =thislist #mylist2 will have same memory location with same content
print(mylist)
mylist = list(thislist) #mylist will have new memory location with same content
#It is also possible to use the list() constructor to make a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#ways to join lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) #['a', 'b', 'c', 1, 2, 3]
#or
for x in list2:
  list1.append(x)
#or
list1.extend(list2)
#sorting
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort() #sorts the list ascending(alphabetically in this this eg) by default.
cars.sort(reverse=True) #descending, Default is reverse=False
def myFunc(e):
  return len(e)

cars.sort(key=myFunc) #A function to specify the sorting criteria(s), here on basis of length of values
print(cars) #['VW', 'BMW', 'Ford', 'Mitsubishi']
cars.sort(reverse=True, key=myFunc) #for DESC

def myFunc1(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc1) #Sort a list of dictionaries based on the "year" value of the dictionaries

#***********************************************************************************************
#Tuple: all methods are almost same as of list, only thing tuple are unchangeable or immutable
#But there is a workaround. You can convert the tuple into a list, change the list, 
# and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
#x[3] = "orange" # This will raise an error
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#To create a tuple with only one item, you have add a comma after the item,
#  unless Python will not recognize the variable as a tuple.
thistuple = ("apple",)
print(type(thistuple)) #tuple

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) #str

thistuple = tuple(("apple", "banana", "cherry")) # tuple using tuple() constructor, note the double round-brackets

#********************************************************SET**************************************************

#*******************************************************SET**************************************************
#Set: A set is a collection which is unordered and unindexed.
#You cannot access items in a set by referring to an index, since sets are unordered the items has no index.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Once a set is created, you cannot change its items, but you can add new items.
print("banana" in thisset) #True

#Add,Remove,Update:

thisset.add("orange") # To add one item to a set use the add() method.
thisset.update(["orange", "mango", "grapes"]) # To add more than one item to a set use the update() method.
print(len(thisset))
thisset.remove("banana") #Note: If the item to remove does not exist, remove() will raise an error.
thisset.discard("banana") #Note: If the item to remove does not exist, discard() will NOT raise an error.
x = thisset.pop() #removes last item, index cannot be passed here in case of set
# Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
thisset.clear()
del thisset

#Join
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) #The union() method returns a new set with all items from both sets
# set1.update(set2) The update() method inserts the items in set2 into set1:
#Note: Both union() and update() will exclude any duplicate items.
#z = x.intersection(y) #The intersection() method returns set which has common values.
#result = x.intersection(y, z) #common of 3 sets

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
#*†****
# declare empty collections:
# mylist = [] or mylist = list()
# mytuple = () or mytuple = tuple()
# myset = set()  // here {} becomes dictionary.
# mydict = {}  or mydict = dict()

#*****************************************DICTIONARY****************************
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

x = thisdict["model"] #access value of given key. or
x = thisdict.get("model") #2nd way to get value of given key
thisdict["year"] = 2018 #change value
thisdict["color"] = "red" #add new item
thisdict.pop("color") #remove
thisdict.popitem() #removes the last inserted item
print(len(thisdict)) #how many items (key-value pairs) a dictionary has

for x in thisdict:
  print(x)  #prints only key
  print(thisdict[x]) #prints value

for x, y in thisdict.items():
  print(x, y) #prints key & value

for x in thisdict.values():
  print(x)   #prints value

#search/contains
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

mydict = thisdict.copy() #copy,new dict
mydict = dict(thisdict)

thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals, use of equals rather than colon for the assignment
print(thisdict)

del thisdict["model"] #remove
thisdict.clear()
del thisdict #delete dict

#nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  }
}
