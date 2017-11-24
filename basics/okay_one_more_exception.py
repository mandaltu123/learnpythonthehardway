try:
    f = open('ac.txt', 'r')
except FileNotFoundError as fnf:
    print("Error {}. Please provide a file that exists".format(fnf))


def factorial(n):
    if n < 0:
        raise ValueError("Negative integer {} do not have factorials".format(n))
    f = 1
    for x in range(2, n + 1):
        f *= x
    return f


try:
    print(factorial(5))
    print(factorial(-5))
except ValueError as ve:
    print(ve)


