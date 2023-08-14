#A program to factorial using recursion
def fact(x):
   if x==0:
      result = 1
   else :
      result = x * fact(x-1)
   return result
print("zero Factorial",fact(2))
print("five factorial",fact(7))
