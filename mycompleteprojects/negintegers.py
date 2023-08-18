if __name__ == '__main__':#Ensures the code executes when run directly and not a module
    n = int(input("Enter number n: "))

    positive_integers = list(range(n))#Ensures the code is positive. The list function converts a range into a list
    for i in positive_integers:
            square =i ** 2
            print(square)



