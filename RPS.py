import time
import random
import sys

x = random.randint(1, 100)
random.seed(x)
print('Seed =', x)

print("")

print('Do you want to play rock, paper, scissors?')
y = str(input())
z = y.lower()

if z == 'yes':
  print("")
elif z != 'yes':
  sys.exit(1)
else:
  sys.exit(1)


print("")

print('How many times do you want to go to?')
times = int(input())

score = 0
cscore = 0


Scissors = 'scissors'
Paper = 'paper'
Rock = 'rock'

#Computer Choice
#rpslist = [Rock, Paper, Scissors]
#cc = (random.choice(rpslist))

print("")


rpslist = [Rock, Paper, Scissors]
cc = (random.choice(rpslist))




for times in range(0, times):
  
  print('Rock, Paper, Scissors')
  rps = str(input())
  x = rps.lower()  
  
  if x == 'rock':
    rpslist = [Rock, Paper, Scissors]
    cc = (random.choice(rpslist))
    if cc == Rock:
      print("You chose", x)
      time.sleep(1)
      print("Computer chose", cc)
      time.sleep(0.2)
      print('You Draw!')
      time.sleep(1)
      score = score+1
      cscore = cscore+1
      print('Your score is', score)
      print('The computers score is', cscore)
      print("")
      print("")

    elif cc == Paper:
      print("You chose", x)
      time.sleep(1)
      print("Computer chose", cc)
      time.sleep(0.2)
      print('You Lose!')
      time.sleep(1)
      cscore = cscore+1
      print('Your score is', score)
      print('The computers score is', cscore)
      print("")
      print("")

    elif cc == Scissors:
      print("You chose", x)
      time.sleep(1)
      print("Computer chose", cc)
      time.sleep(0.2)
      print('You Win!')
      time.sleep(1)
      score = score+1
      print('Your score is', score)
      print('The computers score is', cscore)
      print("")
      print("")

    else:
      print('Error!')



  elif x == 'scissors':
    rpslist = [Rock, Paper, Scissors]
    cc = (random.choice(rpslist))
    if cc == Rock:
      print("You chose", x)
      time.sleep(1)
      print("Computer chose", cc)
      time.sleep(0.2)
      print('You Lose!')
      time.sleep(1)
      cscore = cscore+1
      print('Your score is', score)
      print('The computers score is', cscore)
      print("")
      print("")

    elif cc == Paper:
      print("You chose", x)
      time.sleep(1)
      print("Computer chose", cc)
      time.sleep(0.2)
      print('You Win!')
      time.sleep(1)
      score = score+1
      print('Your score is', score)
      print('The computers score is', cscore)
      print("")
      print("")

    elif cc == Scissors:
      print("You chose", x)
      time.sleep(1)
      print("Computer chose", cc)
      time.sleep(0.2)
      print('You Draw!')
      time.sleep(1)
      score = score+1
      cscore = cscore+1
      print('Your score is', score)
      print('The computers score is', cscore)
      print("")
      print("")

    else:
      print('Error!')



  elif x == 'paper':
    rpslist = [Rock, Paper, Scissors]
    cc = (random.choice(rpslist))
    if cc == Rock:
      print("You chose", x)
      time.sleep(1)
      print("Computer chose", cc)
      time.sleep(0.2)
      print('You Win!')
      time.sleep(1)
      score = score+1
      print('Your score is', score)
      print('The computers score is', cscore)
      print("")
      print("")
    elif cc == Paper:
      print("You chose", x)
      time.sleep(1)
      print("Computer chose", cc)
      time.sleep(0.2)
      print('You Draw!')
      time.sleep(1)
      score = score+1
      cscore = cscore+1
      print('Your score is', score)
      print('The computers score is', cscore)
      print("")
      print("")
    elif cc == Scissors:
      print("You chose", x)
      time.sleep(1)
      print("Computer chose", cc)
      time.sleep(0.2)
      print('You Lose!')
      time.sleep(1)
      cscore = cscore+1
      print('Your score is', score)
      print('The computers score is', cscore)
      print("")
      print("")
    else:
      print('Error!')

  else:
    print('Error! Move Wasted.')
    print("")
    print("")








if score <= cscore:
  print('You Lose!')
  sys.exit

elif score >= cscore:
  print('You Win!')
  sys.exit

elif score == cscore:
  print('You Draw!')
  sys.exit

else:
  print('Error!')
