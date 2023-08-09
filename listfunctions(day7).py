#The common list methods are append,insert,remove,clear,pop(last item in a list), index(existence of a value in a list),in, not in
numbers = [5,3,8,1,6,4,7,2,0,5,7]
# print(numbers.append(9))
# (numbers.insert(0 , 10))
# print(numbers)
# numbers.pop()#Removes the last item in a list
# print(numbers)
# numbers.remove(4)
# print(numbers)
# numbers.clear()
# print(numbers)
# print(numbers.index(5))
# print(50 in numbers)#Checking for existence of 50 in a list
# print(numbers.count(5))
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.reverse()#sorting numbers in descending order
# print(numbers)
# numbers2 = numbers.copy()
# print(numbers2)
# numbers.append(20)
# print(numbers2)
# print(numbers)

#Exercise to remove duplicates in a list
list = [2,3,4,2,3,2,4,7,8,5,6,8,7,0,4,3]
new_list=[]

for numbers in list:
       if numbers not in new_list:
              new_list.append(numbers)
print(new_list)

print("congrats Joyce")
        
    






