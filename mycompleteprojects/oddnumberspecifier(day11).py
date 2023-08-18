#This project is supposed to output a message when a number is odd

number = int(input().strip())


if number % 2 != 0 :
    print("Weird")
elif number % 2 == 0:
    if number in range(2,6):
        print("Not weird")
    elif number in range(6,21):
        print("Weird")
    elif number > 20:
        print("Not weird")

    



