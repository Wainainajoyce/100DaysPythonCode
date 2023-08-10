#This project aims to remove duplicates in a list
my_list = [1,2,3,4,5,6,7,1,2,3,7,8,9,0,0]
# list.sort()
# print(list)
# list.reverse()
# print(list)
# list.append(7)
# print(list)
newlist = []
for numbers in my_list:
    if numbers not in newlist:
        newlist.append(numbers) 
print(newlist)


# #A project to copy the numbers from list to newlist1
# newlist1 = []
# for item in my_list:
#     newlist1.append(item)# To make a copy of the individual elements, you use the append method. The copy method is used to directly copy a list to another list.An exemple is given below.
# print(newlist1)

# #To use the copy method
# # my_list2 = my_list.copy()
# # print(my_list2)

# #The below code prints the item inside the loop, hence in each iteration it prints the original and next.The previous one has only one iteration.
# newlist1 = []
# for item in my_list:
#     newlist1.append(item)# To make a copy of the individual elements, you use the append method. The copy method is used to directly copy a list to another list.An exemple is given below.
#     print(newlist1)







