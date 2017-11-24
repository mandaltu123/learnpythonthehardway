# This is a simple class that will demonstrate how to read and writ to and from a file

input_file = input("please input the file name >> ")
file = open(input_file, 'r') # r is read mode. here we are opening the file in read mode
data = file.read()
print("data in the file \n{}".format(data))
file.close()

# The next section will be about writing something into a file

output_file = input("please provide a file name where you want to white the data >> ")
out_file = open(output_file, 'w')
out_file.write(data)
out_file.close()
print("writing to {} is done".format(output_file))