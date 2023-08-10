# def decimalToBinary(n):
#     return "{0:b}".format(int(n))

# t = decimalToBinary(50)
# print(t)

#The bin function
# t = bin(50)
# print(t)

# binary_string = '110010'
# int_value = int(binary_string,2)#This is a function(int(binary_string))
# print(int_value)

# my_no = "10010010"
# my_value = int(my_no,2)
# print(my_value)


#to convert  a decimal number into binary
value = 47
answer = bytes([value])
print(answer)
integer_value = int.from_bytes(answer, byteorder='big')
print(integer_value)

#learn about struct.pack()


