#The While Loop
#In this guess game, a user should guess a number, if its write the output should be, you won! If the user guesses for 4 times, the output says; Sorry, you failed!Make sure that if the user guesses the right one(9), the game terminates.
secret_number = 20
guess_count = 0
guess_limit = 4
while guess_count < guess_limit :
    guess = int(input("Guess: "))
    guess_count +=1
    if guess == secret_number:
        print("You won!!")
    break
else:
    print("Sorry, you failed!!")





