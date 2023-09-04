import random
import pyautogui
import time
import keyboard

def combo():
    pyautogui.keyDown("w") 
    time.sleep(0.1)
    pyautogui.keyUp("w")
    time.sleep(0.1)
    pyautogui.keyDown("a") 
    time.sleep(0.1)
    pyautogui.keyUp("a")
    time.sleep(0.1)
    pyautogui.keyDown("s") 
    time.sleep(0.1)
    pyautogui.keyUp("s")
    time.sleep(0.1)
    pyautogui.keyDown("d") 
    time.sleep(0.1)
    pyautogui.keyUp("d")
    time.sleep(0.1)
    pyautogui.keyDown("space") 
    time.sleep(0.1)
    pyautogui.keyUp("space")
    time.sleep(0.1)
    pyautogui.keyDown("8") 
    time.sleep(0.1)
    pyautogui.keyUp("8")
    time.sleep(0.1)



g=[1,2,3,4,5,6,7]
t=[0.1,0.2,0.3,0.4]
f=["w","i","s","space","e","i","e","e","e","e","t","space","t","6","t","8","l","9","i","z","b","z","b","b","b","b","z","t","t","f","f","f","f","f"]
random_words = [
    "nigel", "banana boy", "curse bomb", "dog", "nixterinida",
    "frogpose", "calisthenics", "drop the bomb man", "ferry of the kok", "ajanokoji",
    "kite", "lemon", "monkey", "noodle", "orange",
    "bob the penguin", "patata", "sak noobs", "lets baking go", "azuren bulet"
]
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
    elif b=="f":
        combo()
    
    elif b=="i":
        k=random.choice(g)
        if k == 1:
            pyautogui.keyDown(b) 
            time.sleep(0.2)
            pyautogui.keyUp(b)
        pyautogui.mouseDown()
        time.sleep(5)
        pyautogui.mouseUp()

    elif b=="b":

        pyautogui.keyDown(b) 
        time.sleep(0.2)
        pyautogui.keyUp(b)
        pyautogui.mouseDown()
        time.sleep(0.6)
        pyautogui.mouseUp()

    elif b=="z":
        k=random.choice(g)
        pyautogui.keyDown(b) 
        time.sleep(1)
        pyautogui.keyDown(str(k)) 
        time.sleep(0.2)
        pyautogui.keyUp(str(k))
        time.sleep(3)
        pyautogui.keyUp(b)
    elif b=="e":
        k=random.choice(g)
        pyautogui.keyDown(b) 
        time.sleep(0.2)
        pyautogui.keyDown(str(k)) 
        time.sleep(0.2)
        pyautogui.keyUp(str(k))
        time.sleep(3)
        pyautogui.keyUp(b)
    elif b=="t":
        time.sleep(0.1)
        pyautogui.typewrite(random.choice(random_words))
        time.sleep(0.1)
        pyautogui.keyDown("enter")
        time.sleep(0.1)
        pyautogui.keyUp("enter")

    else:
        time.sleep(random.choice(t))
    pyautogui.keyUp(b)
    if keyboard.is_pressed("ctrl"):
        exit()