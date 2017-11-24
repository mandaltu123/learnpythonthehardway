# some more tests on commanline args

from sys import argv

if len(argv) == 3:
    num1 = int(argv[1])
    num2 = int(argv[2])
else:
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))


print("the sum of number1 and number2 is {}".format(num1 + num2))