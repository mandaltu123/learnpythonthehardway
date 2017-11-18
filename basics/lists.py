# This is to demonstrate lists



numbers = [5, 6, 7, 2, 3, 9, 1]
for number in numbers:
    print(number)
"""
Output : 
5
6
7
2
3
9
1
"""

# we can sort this
sortednumbers = sorted(numbers)
print("sorted numbers are {}".format(sortednumbers))

# we have some slicing options too

print("numbers.pop(0) is {} ".format(numbers.pop(0))) # numbers.pop(0) is 5
print("numbers.pop(-1) gives the last element from the list : {}".format(numbers.pop(-1))) # numbers.pop(-1) gives the last element from the list : 1

# append
numbers.append(12)
print("after appending 12 to the list")
for n in range(0, len(numbers)):
    print(numbers[n])


"""
output: [here you will see 5 is missing, because we popped it. pop method removes and returns the item]
6
7
2
3
9
12
"""