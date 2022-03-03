import os
import time
import keyboard
import random
import sys

#Insperation:
#https://replit.com/@InvisibleOne/RandomDungeon?v=1


#https://www.geeksforgeeks.org/keyboard-module-in-python/
#https://pypi.org/project/keyboard/

"""
print("Press any key to continue!")
print("Press 'Esc' to Exit")


if keyboard.add_hotkey('Esc', print, args = ('Exiting...')):


else:
"""

back = True
while back == True:
    if back == True:
        print("1. Start")
        print("2. Settings")
        print("3. Exit")
        print("")
        Starting = input()

    if Starting == '1':
        print("Ok!")

    elif Starting == '2':
        print('Settings:')
        print("")    
        print("")
        print("")
        print("4. Back")
        Setting = input()
        if Setting == '4':
        

elif Starting == '3':
    sys.exit


print("")
time.sleep(3)
clear = lambda: os.system('clsr')
clear()

print("")
