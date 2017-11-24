import os

input_dir = input("Please enter dir to look for files >> ")

for(dirname, subdir, files) in os.walk(input_dir):
    for myfile in files:
        if myfile.endswith('.py'):
            filename = os.path.join(dirname, myfile)

            size = os.stat(filename).st_size
            if 100 <= size <= 1500:
                print("file =>  {} and size => {}".format(myfile, size))