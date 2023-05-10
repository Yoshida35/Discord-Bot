import random

rnd = random.randint(1,6)

while True:
    print("1. Shoot or 2. Quit?")
    x = int(input())
    if x == 1:
        if rnd == 1:
            print("\nYour dead!")
            print("Play again:\n")
            rnd = random.randint(1,6)
        else:
            print("\nSurvived!")
            rnd = rnd - 1
    elif x == 2:
        if rnd == 1:
            print("\nBullet was", rnd, "shot away!")
        else:
            print("\nBullet was", rnd, "shots away!")
        rnd = random.randint(1,6)
    else:
        print("Please enter 1 or 2!")
        print("1. Shoot or 2. Quit?")
        x = int(input())