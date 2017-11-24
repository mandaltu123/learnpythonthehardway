def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero error")
    except Exception as ex:
        print("{}".format(ex))
    else:
        print("result is = {}".format(result))
    finally:
        print("finally")


divide(2, 4)
divide(2, 0)
divide(0, 2)
divide(12, 4.5)