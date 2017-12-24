# 1. Write a program which prints hello world
print("Hello World")

# 2. Write a program which should use following operators
    # a. Addition # b. Subtraction # c. Multiplication # d. Division
a = 2; b = 3; c = a + b
d = (a + b) % ((c * b) - a)
print d

# 4. Write a program using while loop
count = 0
while (count < 3):
    count += 1
    print "Number", count, "is less than the next number"

# 5. Write a program using if else statement
num = 1
if num > 2:
    print "Greater than 2"
elif num:
    print "Got a true statement"
    print num
else:
    print "statement is false"


# 6. Perform following operations on List:
    # a. Concatenation
    # b. Replication
    # c. Updation
    # d. Deletion
list = ["one", "two", "three", 3]

concat = list[0] + " " + list[1]
print concat

replicate = list * 2
print replicate

replicate[4] = 1
replicate[5] = 2

del replicate[4]
del replicate[5]
del replicate[6]

# 7. Write a program to print the current month calendar

import time;
localtime = time.asctime(time.localtime(time.time()) )
print "Local current time :", localtime

import calendar
cal = calendar.month(2017, 1)
print cal

# 8. Write a program of file handling using following methods:
    # a. rename()
    # b. remove()
    # c. mkdir()
    # d. rmdir()
    # e. getcwd()
import os
file_object = open("new_file_name.txt", "wb+")
file_object.close()

os.rename("new_file_name.txt", "exampleFile.txt")

os.remove("exampleFile.txt")

os.mkdir("newdirToDelete")
os.rmdir("newdirToDelete")

os.getcwd()

# 9. Write a program by using match function
import re
line = "Cats are smarter than dogs is proven false"
match = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
print match.group(2)


# 10. Write a program using class concept.
class Dog:
    dogCount = 1
    def __init__(self, name, color):
        self.name = name
        self.color = color
        Dog.dogCount += 1


    def displayDogCount(self):
        print "Dog Count %d" % Dog.dogCount

    def displayDog(self):
        print "Name: ", self.name, ", Color: ", self.color