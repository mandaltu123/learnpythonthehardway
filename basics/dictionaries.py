# Dictionaries are the most commonly used datastructure in python
# They are key value pairs


dic = {1: 'one', 2: 'two', 3: 'three'}

print("print my first dictionary {}".format(dic)) # I did not write dick

# it has keys and values
keys = dic.keys()
values = dic.values()

print("keys are {}".format(keys))
print("values are {}".format(values))

# one way of iteration over dictionary is :
for key in keys:
    print("key = {} and value = {}".format(key, dic.get(key)))



# item() function in dictionary
items = dic.items()
for item, data in dic.items():
    print("the key is {} and the value is {}".format(item, data))


# adding a new item to dictionary
dic[4] = 'four'
print("new dictionary is {} ".format(dic))


# adding a new item with same key
dic[4] = 'iv'
print("adding another item with same key 4 {}".format(dic)) # if you are coming from java background it does the same
# same as like hash table or hashmap it overwrites the old item with the new one



# del operator

del  dic[4]
print("dictionary after deleting 4 {}".format(dic))

