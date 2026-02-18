import random
living = True
location = ""
ids = 0
possbilelocation = ["forest","mountain","ocean"]
possbilestartinglocation = ["forest","mountain","ocean"]
startinglocation = random.randint(0,len(possbilelocation) - 1)
next_location = []
next_location.append(possbilestartinglocation[random.randint(0,len(possbilestartinglocation) - 1)])
location = possbilestartinglocation[startinglocation]
STARTING_EQUIPMENT_COUNT_MAX = 5
STARTING_EQUIPMENT_COUNT_MIN = 3
STARTING_EQUIPMENT_COUNT = random.randint(STARTING_EQUIPMENT_COUNT_MIN,STARTING_EQUIPMENT_COUNT_MAX)
EQUIPMENT_YOU_CAN_GET = [["apple",1],["bread",1],["arrow",1],["ruby,",1],["apple",1],["bread",1]]
equipment = []
living = True
x = ""
STARTING_MAX_HEALTH = 100
max_health = STARTING_MAX_HEALTH
health = STARTING_MAX_HEALTH
death = False
ALL_EQUPIMENT_IN_GAME = [["apple",1],["bread",1],["arrow",1],["ruby,",1]]
def setup():
    if (location == "forest"):
        print("you are in a forest")
    elif (location == "mountain"):
        print("you are in a mountain")
    elif (location == "ocean"):
        print("you are in an ocean")
    adding_thing_to_inventary("dagger")
    for i in range(0,STARTING_EQUIPMENT_COUNT):
        adding_thing_to_inventary(EQUIPMENT_YOU_CAN_GET[random.randint(0,len(EQUIPMENT_YOU_CAN_GET) - 1)][0])
    gameloop(True)
def adding_thing_to_inventary(value):
    equipment.append(value)
    
def check_if_alive(living):
    if (health < 0):
        return False  
    else:
        return True
def action():
    x = input("what do you want to do? press ? for help")
    if (x == "?"):
        return "?"
    elif(x == "exit game"):
        return "exit game"
    elif(x == "check equipment"):
        return "check equipment"
    else:
        return x

def returnanswer():
    returnanswers = int(input())
    return returnanswer
    
def gameloop(living):
    while living == True:
        if (check_if_alive(living) != True):
            living = False
        else:
            living = True
        returnaction = action()
        if (returnaction == "?"):
            print("press exit game to exit game")
            print("check equipment to check equipment")
            print("move to  move location")
        elif (returnaction == "check equipment"):
            print(equipment)
        elif (returnaction == "exit game"):
            living = False
        elif (returnaction == "move"):
            print(f"you can go to {next_location}")
            was = returnanswer()
            if (was == 0):
                location = next_location[was()]
                next_location = []
                for i in range(0,random.randint(1,3)):
                    next_location.append(possbilestartinglocation[random.randint(0,len(possbilestartinglocation) - 1)])
        else:
            print("unacceptable command")



setup()

