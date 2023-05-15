import time
import pyautogui
import webbrowser

x = 0

print("How many bots do you want?")
bots = int(input())
print("What is the game pin?")
pin = str(input())
print("Type a name:")
botname = str(input())

for i in range(bots):
    x=str(x)
    botname = (botname+x)
    botname = str(botname)
    x = int(x)
    website = "https://kahoot.it/"
    webbrowser.open(website, new=0, autoraise=True)
    time.sleep(1)
    pyautogui.moveTo(960, 600)
    pyautogui.click()
    pyautogui.write(pin)
    pyautogui.moveTo(960, 630)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(960, 620)
    pyautogui.click()
    pyautogui.write(botname)
    pyautogui.moveTo(960, 670)
    pyautogui.click()
    x = x + 1
