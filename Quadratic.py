import time
import math

print("What is a?")
a = int(input())
print("")

print("What is b?")
b = int(input())
print("")

print("What is c?")
c = int(input())
print("")

bs = b*b
#b squared

#nb = b-(2*b)
nb = 0-b
#negative b

x = bs - (4*a*c) / (2*a)

Positive = nb + math.sqrt(x)

time.sleep(1)
print("")

Negative = nb - math.sqrt(x)

print(Positive)
print(Negative)
input("Press Enter to Exit:")
