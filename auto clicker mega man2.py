import time
import threading
from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Controller, Button

TOGGLE_Key = KeyCode(char="`")
clicking = False
mouse = Controller()
def clicker():
    while True:
        if clicking:
            mouse.click(Button.left,1)
        time.sleep(0.0000001)
def toggle_event(key):
    if key == TOGGLE_Key:
        global clicking
        clicking = not clicking
click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()