#The program below receives credit card information and returns whether its a string or integer.
"""Card Number
Cardholder Name
Expiration Date
Security Code
Cardholder's Address"""

cardnumber = int(input("Enter the card number: "))
cardholdername = input("Enter the card holder name: ")
securitycode = int(input("Enter the securitycode: "))
cardholderaddress = input("Enter the card holder address: ")


def datTypey(a):
    datatype = type(a)
    return(datatype)


cardnumberd_type = datTypey(cardnumber)
print(cardnumberd_type)
cardholder_type = datTypey(cardholdername)
print(cardholder_type)
securitycode_type = datTypey(securitycode)
print(securitycode_type)
address_type = datTypey(cardholderaddress)
print(address_type)




