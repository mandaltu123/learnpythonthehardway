# we will demonstrate some exceptions here

while True:
    try:
        x = int(input("Please enter a number : "))
        print("{} is a valid input".format(x))
        break
    except ValueError:
        print("Oops! That was not a valid number. Please try again...")
    except Exception as genericException:
        print("{} exception caught ".format(genericException))


def this_fails():
    x = 1/0


try:
    this_fails()
except ZeroDivisionError as generic:
    print("{} exception caught".format(generic))




