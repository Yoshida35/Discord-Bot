import sys
import random

number = random.randint(1, 10)

print("Guess a number from 1 to 10!")

guess = int(input())



if guess != number:
    while guess != number:
        print("Guess again!")
        guess = int(input())
        print("")

else:
    print("Correct!")
    sys.exit
