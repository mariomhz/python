# number guesser
import random
print("welcome to the random number guessing game!")
secret_num = random.randint(1, 100)
guess = None
while guess != secret_num:
    guess = int(input("guess a number between 1 and 100: "))
    if guess < secret_num:
        print("too low! try again.")
    elif guess > secret_num:
        print("too high! try again.")
    else:
        print("congratulations! you guessed it!")