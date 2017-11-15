# This will demonstrate usage of else and if together


people = 30
cars = 40
buses = 15

if cars > people:
    print("we should take the cars")
elif cars < people:
    print("we should not take the cars")
else:
    print("we can't decide")

if buses > cars:
    print("That's too many buses")
elif buses < cars:
    print("May be we could take the buses")
else:
    print("we still can't decide")

if people > buses:
    print("alright, let's just take the buses")
else:
    print("Fine let's just stay at home")

