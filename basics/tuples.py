# Tuples are like lists but unmodifiable and
"""
A tuple is a fixed size grouping of elements, such as an (x, y) co-ordinate. Tuples are like lists, except they are
immutable and do not change size (tuples are not strictly immutable since one of the contained elements could be
mutable). Tuples play a sort of "struct" role in Python -- a convenient way to pass around a little logical, fixed
size bundle of values. A function that needs to return multiple values can just return a tuple of the values.
For example, if I wanted to have a list of 3-d coordinates, the natural python representation would be a list of
tuples, where each tuple is size 3 holding one (x, y, z) group.

"""



tuple = (1, 2, 'hi')
print(tuple)
print("length of the tuple is {} ".format(len(tuple)))
print("tuple[2] = {}".format(tuple[2]))
# iteration over tuple

for element in tuple:
    print(element)


(x, y, z) = (30, 45, 60)
print("values of x = {} y = {} and z = {}".format(x, y, z))


# tuples are immutable, the bellow code does not run
# tuple[2] = 'bye'

tuple = (1, 2, 'bye')

print(tuple)


