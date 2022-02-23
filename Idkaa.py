import random
import sys

random.seed()
number = random.randint(1000, 9999)
print(number)
print("")

print("Guess the 4 digit Number!")

number = str((number))

a = number[0]
b = number[1]
c = number[2]
d = number[3]

while True:
    guess = input()

    if number == guess:
        print("You got it right!")
        sys.exit


    elif guess == a:
        print("You got 1 digit right!")

    elif guess == b:
        print("You got 1 digit right!")

    elif guess == c:
        print("You got 1 digit right!")

    elif guess == d:
        print("You got 1 digit right!")

    else:
        print("Guess again!")
