#Membership operators test for membership in lists, sequences or tuples.
a = 10
b = 2
c = b * a

list = [3,5,6,9,2,4,10,20,45]
if a in list:
    print("a is available in the given list")
else:
    print("a is not available in the given list")

if b not in list:
    print("b is not in the given list")
else:
    print("b is available in the given list")

if c in list:
    print("There is a multiple of both a and b")
else:
    print("The given list is not a multiple of both a and b")

