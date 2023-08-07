names = [ "joyce" , "cate" , "Velma" , "Maggy" , "Hannah"]
print(names[2:5])
print(names[2])
print(names[2:])
names[0]= "jon"#Updating or changing a list item
print (names)

#Exercise to find the largest number in a list
numbers = [ 1,3,6,7,9,3,5,7]
print(max(numbers))

#or
numbers = [ 1,3,6,7,9,3,5,7]
max = 1
for number in numbers:
    if number > max:
        max = number
print(max)
