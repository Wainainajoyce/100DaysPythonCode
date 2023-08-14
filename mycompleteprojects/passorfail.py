#This program returns a pass or fail
def result(a):
   if a>40:
      return ("pass")
   else:
      return "fail"
a=int(input("Enter one subject marks: "))
print(result(a))