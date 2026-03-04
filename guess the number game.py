import random
number = random.randint(0,1000)
good = 0
bad = 0
all = 0
try:
    asnwer = int(input("guess the number ranges from 0 to 1000"))
except ValueError:
    print("not acceptable")
while (asnwer != number):
    if (asnwer < number):
        print("too low")
        bad += 1
    if (asnwer > number):
        print("too high")
        bad += 1
    try:
        asnwer = int(input("guess the number ranges from 0 to 1000"))
    except ValueError:
        print("not acceptable")
if (asnwer == number):
    print("you got it")
    good += 20
all = good + bad
if (good/all > 0.9):
    print("rank S")
elif(good/all > 0.7):
    print("rank A")
elif(good/all > 0.5):
    print("rank B")
elif(good/all > 0.3):
    print("rank C")
elif(good/all > 0.1):
    print("rank F")
else:
    print("you are so bad I can't give you a rank")

