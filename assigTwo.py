#1.Write a sample Python code to write a file?

file_object = open("new_file_name.txt", "wb+")
file_object.write("Hello World!\nJust created a sample Python code to write a file")
file_object.close()


print "Name of the file: ", file_object.name
print "Closed or not : ", file_object.closed
print "Opening mode : ", file_object.mode
print "Softspace flag : ", file_object.softspace


#2. Write a sample Python code to open  database?
