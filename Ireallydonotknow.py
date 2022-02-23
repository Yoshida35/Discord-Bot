import random
import time

#Higher Stamina goes first unless same / draw then player goes for easy bosses, random for medium bosses and boss for hard bosses.

seed = random.randint(1, 100)
random.seed(seed)
print("Seed:", seed)
print("")

x = random.randint(2, 3)
y = random.randint(8, 12)
z = random.randint(2, 3)

attack = x
health = y
stamina = z
money = int(0)

print("What is your name Dungeon Explorer?")
name = input()

time.sleep(1)

print("")

print("Your Stats are:")
print("Attack: ", attack)
print("Health: ", health)
print("Stamina: ", stamina)
print("Money: ", money)

print("")
input("Please press enter to continue.")
print("")

print("You find a sword!")
attack = attack+random.randint(2, 3)
print("Your attack is", attack)

print("")
input("Please press enter to continue.")
time.sleep(1)
print("")

#seal's attack, health and stamina.
sa = 1
sh = random.randint(6, 10)
ss = random.randint(1, 2)



if ss > stamina:
    print("The seal sees you first!")
    print("")
    while sh > 1:
        time.sleep(1)
        if sh > 1:
          health = health-sa
          print("The seal slaps you! Your health is ", health)
          print("")
        time.sleep(1)
        if sh > 1:
          sh = sh-attack
          if sh < 1:
            print ("You slay the seal with a final blow to the head!")
            win = True
          else:
            print("You counter attack. The seals health is ", sh)
            print("")
            win = False
        print("")


if ss < stamina:
    print("You attack the seal first!")
    print("")
    while sh > 1:
        time.sleep(2)
        if sh > 1:
          sh = sh-attack
          if sh < 1:
              print ("You slay the seal with a final blow to the head!")
              win = True
          else:
            print("You hit the seal! The seals health is ", sh)
            print("")
            win = False
        time.sleep(2)
        if sh > 1:
          health = health-sa
          print("The seal counter attacks. Your health is ", health)
          print("")
        print("")


if ss == stamina:
    print("You attack the seal first!")
    print("")
    while sh > 1:
        time.sleep(2)
        if sh > 1:
          sh = sh-attack
          if sh < 1:
              print ("You slay the seal with a final blow to the head!")
              win = True
          else:
            print("You hit the seal! The seals health is ", sh)
            print("")
            win = False
        time.sleep(2)
        if sh > 1:
          health = health-sa
          print("The seal counter attacks. Your health is ", health)
          print("")
        print("")

if seed == -1:
    print("")

elif health == 0:
  print("Try again...")

else:
    if win == True:
        money = money+random.randint(5, 7)
print("Well Done Dungeon Explorer...")
time.sleep(1)
print("Sorry, I mean", name, "...")
time.sleep(2)
print("Anyway, have I told you about the shop?")
input()
time.sleep(0.5)
print("Well, there is a shop...")
time.sleep(0.5)
print("It only sells three things:")
time.sleep(0.5)
print("1. Health Potion, 2. Stamina Potion, 3. Attack Potion")
time.sleep(1)
print("Health Potion increases health by +1, Stamina Potion increases stamina by +1, Attack Potion increases attack by +1")
time.sleep(3)
print("Potions cost £5, you have £", money)
time.sleep(2)

print("Please choose '1', '2', '3' or 'n' for nothing.")
shop1 = input()
if shop1 == '1':
    money = money-5
    Health_Potion = health+1
    print("Your health is now", health)

elif shop1 == '2':
    money = money-5
    Stamina_Potion = stamina+1
    print("Your stamina is now", stamina)

elif shop1 == '3':
    money = money-5
    Attack_Potion = attack+1
    print("Your attack is now", attack)

else:
    print("")


print("")

print("Your Stats are:")
print("Attack: ", attack)
print("Health: ", health)
print("Stamina: ", stamina)
print("Money: ", money)
