import random
import sys

print("How many Dice do you want?")
DiceAmounts = int(input())

x = 0

while x != DiceAmounts:
  Dice = random.randint(1, 6)
  print(Dice)
  x += 1

else:
  sys.exit
