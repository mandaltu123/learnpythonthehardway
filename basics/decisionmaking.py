# Now that we have seen how if, elif and else work together we can possibly write some script that can
# decide what to do and what not to


print("You enter a dark room with two doors. Do you take #door1 or #door2 ?")
door = input(">> 1 or 2 ?")

if door == "1":
    print("There's a giant beer here eating a cheese cake. What do you do ?")
    print("1. Take the cake")
    print("2. Scream at the bear")

    bear = input(">> 1 or 2 ?")
    if bear == "1":
        print("the bear eats your face off, good job!")
    elif bear == "2":
        print("The bear eats your legs off, good job!")
    else:
        print("well doing {} is better. Bear runs away".format(bear))

elif door == "2":
    print("You enter the endless abyss at Cthulu's retina. No Idea what the fuck this means. Copied from book")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins")
    print("3. Understanding revolver yelling melodies")

    insanity = input(">")
    if insanity == "1" or insanity == "2":
        print("your body survives")
    else:
        print("you are kinda doomed")

else:
    print("you stumble around and fall on a knife, you are dead!")