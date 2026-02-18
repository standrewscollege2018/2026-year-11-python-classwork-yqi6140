# this is a program
import random
wa = "n"
answer = ""
xs = 2
ABAT =["a","b","c","d","e","f","g","h","i","j","k","l","m","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
def do_it(answer):
        print(f"your contry is {answer[0:2]}")
        print(f"your manufacturer is {answer[2:7]}")
        print(f"your product code is {answer[7:12]}")
        print(f"your check  is {answer[12:13]}")
def checkifvaided(answer,israndom):
    if (len(answer) < 13):
        print("your bar code is invaided")
    elif(israndom == True):
        print(f"your random bar code is " + answer)     
        do_it(answer)
    else:
        print("your bar code is vaided")
        do_it()
2
def ca():
    answer = ""
    for i in range(0,13):
        xs=random.randint(0,len(ABAT) - 1)
        wa=ABAT[xs]
        answer += wa
    checkifvaided(answer,True)    
while True:
    humananswer = input("make random bar code or enter one press 1 for the first 2 for the second ")
    if (humananswer == "1"):
        ca()
        break
    elif(humananswer == "2"):
        humananswer = input("what is your bar code")
        checkifvaided(humananswer,False) 
        break
    else:
        print("invaided answer")
        
