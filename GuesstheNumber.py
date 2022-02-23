import time
import random #dunno why i still have this but imma keep it just in case

random.seed()
cn = random.randint(1, 10)
#print(cn)
#^^^^^^^^^ if i wanna see what the cn is before

#cn = ComputerGeneratedNumber

print("I'm thinking of a number from 1 to 10, guess!")


while True:

    guess = int(input())
    
    if guess == cn:
        print("Winner, you are Correct, the number was", cn, "!")
        break

    elif guess != cn:
        print("Guess again!")
