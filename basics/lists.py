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

# while loop
# write a program to print every third element from a list

mylist = [1, 3, 4, 5, 44 ,6 ,7, 8, 8, 11 , 66, 77, 88, 95]
count = 0
print("print every 3rd element form the list : {}".format(mylist))
while count < len(mylist):
    print("element {}th value : {} ".format(count, mylist[count]))
    count = count + 3


"""

examples from: https://developers.google.com/edu/python/lists
list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
list.sort() -- sorts the list in place (does not return it). (The sorted() function shown below is preferred.)
list.reverse() -- reverses the list in place (does not return it)
list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
"""

list = ['larry', 'curly', 'moe']
list.append('shemp')  ## append elem at end
list.insert(0, 'xxx')  ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print(list.index('curly'))  ## 2

list.remove('curly')  ## search and remove that element
list.pop(1)  ## removes and returns 'larry'
print(list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']


# some more sorting

strs = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs))  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print(sorted(strs, reverse=True))  ## ['zz', 'aa', 'CC', 'BB']


# custom sorting with key


st = ['oooooo', 'aa', 'XXX', 'KKK', 'uuuu', 'dd']
print(sorted(st, key=len))


# we can also pass in a function as a key

str = ['xc', 'zb', 'yd' ,'wa']


"""This function returns last alphabet from the passed in words"""
def myFn(s):
    return s[-1]


print("sorted based on the last alphabet of the word {}".format(sorted(str, key=myFn)))


