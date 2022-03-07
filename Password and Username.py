import time
import random


x = random.randint(1, 100)
random.seed(x)
print('Seed =', x)

time.sleep(1)
print("")

print('Please Enter your username:')
username = input()

time.sleep(1)
print("")

passlist = ('A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z')


first = str(random.choice(passlist))
second = str(random.choice(passlist))
third = str(random.choice(passlist))
fourth = str(random.choice(passlist))
fith = str(random.choice(passlist))
sixth = str(random.choice(passlist))

passlist2 = ("'", '@', ';', ':', '.', ',', '#', '~', '[', ']', '{', '}', '=', '-', '+', '_', '?', '/', '|', '`', '¬', '¦', '(', ')', '!', '"', '£', '$', '%', '^', '&', '*', '>', '<')
seventh = str(random.choice(passlist2))

eigth = str(random.randint(0, 9))
ninth = str(random.randint(0, 9))
tenth = str(random.randint(0, 9))
eleventh = str(random.randint(0, 9))

passlist2 = ("'", '@', ';', ':', '.', ',', '#', '~', '[', ']', '{', '}', '=', '-', '+', '_', '?', '/', '|', '`', '¬', '¦', '(', ')', '!', '"', '£', '$', '%', '^', '&', '*', '>', '<')
twelvth = str(random.choice(passlist2))

time.sleep(1)

password = (first + second + third + fourth + fith + sixth + seventh + eigth + ninth + tenth + eleventh + twelvth)
print('Your username is:', username)
print('Your suggested Password:', password)

print("")

time.sleep(1)

print('Re-enter your Password:')
passcheck = input()

y = True

while y == True:
    if passcheck != password:
        print('Try and enter it again!')
        passcheck = input()

    else:
        print('Make sure you save it for next time!')
        input("Press Enter to end:")
        break