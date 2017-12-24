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
localtime = time.asctime( time.localtime(time.time()) )
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
# 9. Write a program by using match function
# 10. Write a program using class concept.