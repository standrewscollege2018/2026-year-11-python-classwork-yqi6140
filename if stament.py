x = (input("What is the password"))
w = 0
T = 0
while True:
    z = False
    if (x == "10203"):
        z = True
    if (z == True):
        print("you have passed")
        break
    else:
        print("not correct")
        w += 1
        if (w < 3):
            x = input("would you like to try again YES OR NO")
            T = x.lower()
            if (T == "yes"):
                x = input("What is the password")
            elif (T == "no"):
                print("good bye")
                break
            else:
                print("you have not answer an acceptable answer")
                break
                
        else:
            print("you have tried too many times")
            break
        