# File Handling: open() function is used in file handling.
# The open() function takes two parameters; filename, and mode.

# 4 different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist //default
# "a" - Append - Opens a file for appending(to the end of the file), creates file if it dznt exist.
# "w" - Write - Opens a file for writing(overwrite any existing content), creates file if it dznt exist
# "x" - Create - Creates the specified file, returns an error if the file exists

#above are 3 ways to create a file

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode //default
# "b" - Binary - Binary mode (e.g. images)

# f = open("demofile.txt") is same as:  f = open("demofile.txt", "rt")
import os
import sys

print("root directory is:",os.path.abspath(os.curdir)) #C:\GitCode\python-concepts-dkv
print("current file absolute path:",os.path.abspath(__file__)) #C:\GitCode\python-concepts-dkv\code\file-handling.py


f = open(os.path.abspath(os.curdir)+"\\code\\test-data\\demofile.txt", "r")
print(f.read()) #returns the whole text of file(all lines of file)
print(f.read(5)) # returns just 5 characters
print(f.readline()) #reads first line
print(f.readline()) #reads 2nd line

for x in f: #read the whole file, line by line
  print(x)

f.close()  #good practice 

# Note: You should always close your files, in some cases, due to buffering, 
# changes made to a file may not show until you close the file.

#append
import datetime

dt = datetime.datetime.now()
 #formatting date objects into readable strings : strftime()
 
print("current date time: ",dt) #2020-04-10 22:30:05.562953
print("current year: ",dt.year) #2020
print("current day: ",dt.strftime("%A")) #Friday
print("current day: ",dt.strftime("%a")) #Fri
print("current month: ",dt.strftime("%B")) #April
print("current month: ",dt.strftime("%b")) #Apr
print("current year: ",dt.strftime("%Y")) #2020
print("current year: ",dt.strftime("%y")) #20
print("current year: ",dt.strftime("%d-%m-%Y:%H-%M-%S %p")) #dd-mm-yyyy: 10-04-2020:22-38-25 PM

f = open(os.path.abspath(os.curdir)+"\\code\\test-data\\appenddemofile.txt", "a")
f.write(" Now the file has more content!: "+ str(datetime.datetime.now()))
f.close()

#open and read the file after the appending:
f = open(os.path.abspath(os.curdir)+"\\code\\test-data\\appenddemofile.txt", "r")
print(f.read())

#write
f = open(os.path.abspath(os.curdir)+"\\code\\test-data\\writedemofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open(os.path.abspath(os.curdir)+"\\code\\test-data\\writedemofile.txt", "r")
print(f.read())

#create empty file
f = open("create-emptyfile.txt", "x")
f.close()

import os
if os.path.exists("create-emptyfile.txt"):
  os.remove("create-emptyfile.txt")
else:
  print("The file does not exist")

 #os.rmdir("myfolder") # remove only an empty folder