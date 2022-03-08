import random
import time

print("What is your name")
Name = str(input("Name: "))
time.sleep(1)
print("Hello", Name)

random.seed(Name)

print("")
time.sleep(1)

print("How old are you?")
age = int(input("Age: "))
time.sleep(1)
print("I am", random.randint(1,100), "Years Old!")

print("")
time.sleep(1)

print("What's your favourite number?")
favNumber = int(input())
rng = random.randint(0, 6942069420) #Don't question it.
print("My favourite number is", rng)

time.sleep(1)

listOfFruits = list(['Apple', 'Bannana', 'Orange', 'Mango', 'Advocado'])
computerFavFruit = random.choice(listOfFruits)
print("Also my favourite fruit is", computerFavFruit)
time.sleep(2)
print("What's your favourite type of fruit?")
favFruit = str(input())
time.sleep(1)
print("That's good.")
print("")

time.sleep(1)

print("Do you have any friends? (Please enter 'Yes' or 'No'!)")
friends = str(input())
if friends == 'Yes':
    print("What is their name?")
    friend = input("Friend: ")
    print("I know", friend, "too!")

elif friends == 'No':
    print("You'll find some...")

else:
    print("Please Enter 'Yes' or 'No' next time!")

time.sleep(1)
print("")

print("What is the day today?")
day = input("Day: ")
print("It is", day, "Today!") #Just go along with it.

time.sleep(1)
print("")

print("What is the time today?")
time = input("Time: ")
print("It is", time, "Today!") #Just go along with it.

import random
import time

print("")
time.sleep(1)
#idk how to fix the 'str' object has no attribute 'sleep'"

print("What do you like doing?")
likesDoing = input()
print("I like talking but more important listening!")


print("")
time.sleep(1)


print("Anyway Moving on \n ...")

random.seed()
cn = random.randint(1, 10)
#print(cn)
#^^^^^ if i wanna see what the cn is before

#cn = ComputerGeneratedNumber

print("I'm thinking of a number from 1 to 10, guess!")


while True:

    guess = int(input())
    
    if guess == cn:
        print("Winner, you are Correct, the number was", cn, "!")
        break

    elif guess != cn:
        print("Guess again!")
