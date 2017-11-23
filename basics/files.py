# This is a simple class that will demonstrate how to read and writ to and from a file

input_file = input("please input the file name >> ")
file = open(input_file, 'r') # r is read mode. here we are opening the file in read mode
print(file.read())
file.close()