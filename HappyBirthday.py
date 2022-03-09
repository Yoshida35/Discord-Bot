import datetime
import time
import sys

datenow = datetime.datetime.now()

print('What year were you born on?')
BY = int(input())
time.sleep(1)

print('What month were you born on?')
BM = int(input())
time.sleep(1)

print('What day of the month were you born on?')
BD = int(input())
time.sleep(1)


x = int(datenow.month)
y = int(datenow.day)

if BM == x:
  if BD == y:
    print("Happy Birthday!")
  else:
    sys.exit(1)
else:
  sys.exit(1)
