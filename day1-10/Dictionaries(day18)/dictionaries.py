# #Dictionaries are used to list key value pairs. A customer may have attributes, hence the attribute and the value of the attribute.
# #One can use both strings and numbers
# #Each key should be unique

# student = {
#     "name":"Joy Mwendo",
#     "course": "Communication and computer networks",
#     "age" : 20
# }

# print(student["name"])#One can use the square brackets to list the student value or........., if the key value is not present it returns an error.
# #You can also use the get method which if the key value does not exist it returns none.
# #By using the get method, you can also specify a value to return if the birthdate doies not exist
# print(student.get("name"))

# print(student.get("birthdate"))
# print(student.get("birthdate","1 January 2023"))

# #Can also update a value
# student["name"] = "John Kim"
# print(student["name"])

# #or a key, this is more like adding another key value pair
# student["major"] = "ICT"
# print(student["major"])

# print(student)

#Exercise
#Write a program to ask for a phone number and it outputs the phone number in words

#Using dictionaries
phone = input("phone: ")

digit_mapping = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
output = ""

for char in phone:
    output += digit_mapping.get(char, "!") + " "
print(output)

# from num2words import num2words
# phone_number = input("Phone number: ")


# for i in phone_number:
#     print(num2words(i))

# print("well done chatgpt!!!! and Joyce haha")


# from num2words import num2words

# phone_number = input("Phone number: ")


# #Can also prompt the program to check if the number is a digit first

# for digit in phone_number:
#     if digit.isdigit():  # Check if the character is a digit
#         word_representation = num2words(int(digit))
#         print(word_representation)
#     else:
#         print("Not a digit:", digit)











