import keyboard
import time
clicking = False
going = False
swap = False
while going == False:
    if keyboard.is_pressed("q"):
        break
    if keyboard.is_pressed("c"):
        keyboard.press("t")
        keyboard.release("t")
        time.sleep(0.001)
    #if not keyboard.is_pressed("c"):
        #keyboard.press("t")
        #if keyboard.is_pressed("q"):
           # going = True   