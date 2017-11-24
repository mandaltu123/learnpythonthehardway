def average(*args):
    """
    *args can take n number of inputs of any type as long as operation on them is valid
    the input is a type of tuple
    :param args: n number of same type
    :return: returns average of input numbers
    """

    if len(args) < 2:
        print("wow you genious , do you even know what average means ?")
        return

    # print(type(args)) --> this prints : <class 'tuple'>
    print("Average of {} is {}".format(args, sum(args) / len(args)))


average(4, 5)
average(4, 5, 6)
average(3.4, 5.6)
average()
average(1)