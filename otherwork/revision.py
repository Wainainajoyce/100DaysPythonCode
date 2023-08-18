# print("My name is %s and weight is %d kg!" % ('Zara' , 21))

# str1 = """
# This is a long string that is made up of several lines
# and non-printable characters such as tab (\t)nad they will show up that way when 
# displayed.New line is given within square brackets [\n]
# """
# print(str1)
# hey = "hello Joyce"
# print(hey.capitalize())
# print(hey.islower())

# str = "this is a string exampe...wow!!!"
# print("str.center(40, 'a') :", str.center(40, 'a'))


# str = "this"
# # No space & digit in this string
# print (str.isalpha())
# str = "this is string example....wow!!!"
# print (str.isalpha())

# str = "123456";
# # Only digit in this string
# print (str.isdigit())
# str = "this is string example....wow!!!"
# print (str.isdigit())

str = "This Is String Example...Wow!!!"
print (str.istitle())
str = "This is string example....wow!!!"
print (str.istitle())

s = "-"
seq = ("a", "b", "c") # This is sequence of strings.
print (s.join( seq ))

str = "this is string example....wow!!!"
print ("Length of the string: ", len(str))

#ljust
str2 = "this is string example....wow!!!"
print (str2.ljust(50, '*'))

str = "THIS IS STRING EXAMPLE....WOW!!!"
print (str.lower())

str = ""
#this is string example....wow!!!"
print (str.lstrip())
str = "*****this is string example....wow!!!*****"
print (str.lstrip('*'))

#The maketrans method translates characters in the intab to the outtab string.
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
str = "this is string example....wow!!!"
print (str.translate(trantab))


#maximum character.In the following example it gives the highest index
str = "this is a string example....really!!!"
print ("Max character: " + max(str))
str = "this is a string example....wow!!!"
print ("Max character: " + max(str))


#Minimum character.In this example it gives the minimum index.
str = "www.tutorialspoint.com"
print ("Min character: " + min(str))
str = "TUTORIALSPOINT"
print ("Min character: " + min(str))


#Replaces the former to latter.
str = "this is string example....wow!!! this is really string"
print (str.replace("is", "was"))
print (str.replace("is", "was", 3))
