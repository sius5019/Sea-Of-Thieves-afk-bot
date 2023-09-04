import random
import pyautogui
import time
import keyboard
g=[1,2,1,1,1]
t=[0.1,0.2,0.3,0.4]
f=["w","i","s","space","i","space","6","8","l","9","i","z","z","z"]
time.sleep(3)
while True:
    b=random.choice(f)
    pyautogui.keyDown(b) 
    if b=="8":
        pyautogui.mouseDown()
        time.sleep(2)
        pyautogui.mouseUp()
    elif b=="l":
        pyautogui.mouseDown(button="right")
        time.sleep(2)
        pyautogui.mouseUp(button="right")
    elif b=="i":
        k=random.choice(g)
        if k == 1:
            pyautogui.keyDown(b) 
            time.sleep(0.2)
            pyautogui.keyUp(b)
        pyautogui.mouseDown()
        time.sleep(6)
        pyautogui.mouseUp()
    elif b=="z":
        k=random.choice(g)
        pyautogui.keyDown(b) 
        time.sleep(2)
        if k == 1:
            pyautogui.keyDown("1") 
            time.sleep(0.2)
            pyautogui.keyUp("1")
            time.sleep(5)
            pyautogui.keyUp(b)
        else:
            pyautogui.keyDown("2") 
            time.sleep(0.2)
            pyautogui.keyUp("2")
            time.sleep(5)
            pyautogui.keyUp(b)
    else:
        time.sleep(random.choice(t))
    pyautogui.keyUp(b)
    if keyboard.is_pressed("ctrl"):
        exit()