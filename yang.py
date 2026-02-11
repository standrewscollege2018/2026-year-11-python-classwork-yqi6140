# this is a program

import random
wa = "n"
xs = 2
abat =["a","b","c","d","e","f","g","h","i","j","k","l","m","o","p","q","r","s","t","u","v","w","x","y","z"]
print("hellow World")
if (xs == 2):
    print (" hi this is a precorded message")
def xw():
    while True:
        xs=random.randint(0,24)
        if (xs == 24):
            break
        wa=abat(xs)
        print(wa)     
xw()
