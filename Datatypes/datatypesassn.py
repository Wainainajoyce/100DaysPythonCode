#Output of the given code.X in the inner function is changed into 25 but in the outer block x is 50
# x = 50
# def fun1():
#     x = 25
#     print(x)
# fun1()
# print(x)


# def myfunc(a):
#     a = a + 1
#     return a
# b = 3
# c = myfunc(b)
# print(c)

# x = 75
# def myfunc()
#     x=x+1
#     print(x)
# myfunc()
# print(x)
  
#Output of the following block of code
"""According to the output, tha first one is false while the rest are True
This is because the bool function tests an input for true or false. 
The false values are false, zero,none,Empty sequences (lists, tuples, strings)
Empty dictionaries
Empty sets
Custom objects without a defined __bool__() or __len__() method """

print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

#To get to know the datatype of an input use the type method
val1 = 50
data1 = type(val1)
print(data1)

print(type(0xFF))
print(type("I am a lady"))
print(type(False))




