#Operations on strings and their creation
str1 = "My name is Joyce"
str2 = "My name is Austin"
print(str1)
print(str2)

#Length
print(len(str1))
print(len(str2))
#can also put it in a variable
len1 = len(str1)
print(len1)

#upper operation
print(str1.upper())
print(str2.upper())

#Lower operation
print(str1.lower())
print(str2.lower())

#The split method. When applied it gives a result as a list
split1 = str1.split()
print(split1)

#replace method
a = "Joyce"
b = a.replace("Joyce", "Wairimu")
print(b)

replace1 = "My school is the technical university of kenya"
replace2 = replace1.replace("school","campus")
print(replace2)

#The strip method
hey1 = " i really like saying hello"
print(hey1.strip())

#Concatenation
mystr = "I am a python developer."
mystr1 = " I love coding in python"

#method1 +
mystr2 = mystr + mystr1
print(mystr2)

#Can also use the join method 
mystr3 = ''.join([mystr,mystr1])
print(mystr3)








