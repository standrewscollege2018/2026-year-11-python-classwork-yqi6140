listy = []
listy2 =[]
id = 1
idremover = 0
looping = True
bigx = -1
bigZero = "0"
check = 0
checking = ""
answer =""

def sort():
    check = 0
    for i in range(0,len(listy2)):
        listy[check].id = check + 1
        check += 1
class student:
    def __init__(self,gender,height,name,id):
        self.gender = gender
        self.height = height
        self.name = name
        self.id = id
        listy.append(self)
    def get_height(self):
        return self.height
    def get_gender(self):
        return self.gender

student("female",1.45,"John ana",id)
id += 1

student("male",1.7,"Yang",id)
id += 1

student("male",2,"Brosn",id)
id += 1

student("male",1.2,"Mikey mouse",id)
id += 1

student("male",1.9,"Derrack",id)
id += 1

student("female",1.4,"Catteran",id)
id += 1

student("male",1.5,"Lucas",id)
id += 1

student("male",1.6,"Katen",id)
id += 1

student("male",1.6,"Hareeson",id)
id += 1

student("male",1.9,"Dan",id)
id += 1

student("male",2,"Mr Adams",id)
id += 1

student("male",1.9,"terranse",id)
id += 1

student("male",1.65,"anstory",id)
id += 1

student("male",2.2,"noodles",id)
id += 1

student("male",1.3,"benji u",id)
id += 1

student("male",1.32,"reese",id)
id += 1

student("male",1.6,"medusa",id)
id += 1 

student("male",2.5,"spencer",id)
id += 1
while (looping == True):
    try:
        answer = input("what do you wan to do check students add students or remove students or stop all")
    except ValueError:
        print("stop being stupid")
    if (answer == "check students"):
        try: 
            bigx = int(input(f"pick 1 to {len(listy)}"))
            bigZero = "2"
        except ValueError:
            print("stop being stupid")
            bigx = -1
        #try: 
            #bigZero = input("pick one of the options gender height name")
        #except ValueError:
            #print("stop being stupid")
            #bigZero = "2"
        #if (bigx != -1 and bigZero != "0"):
            #looping = False
        if (bigx == 0):
            looping = False
        if (bigx < len(listy) + 1 and bigx > 0):
            print(f"height {listy[bigx - 1].height} name {listy[bigx - 1].name} gender {listy[bigx - 1].gender}")
        #if (bigZero == "gender"):
        # print(listy[bigx - 1].gender)
        #elif (bigZero == "height"):
            #print(listy[bigx - 1].height)
        #elif (bigZero == "name"):
            #print(listy[bigx - 1].name)
        #else:
            #print("not allowed")
        else:
            print("stopping")
            looping = False
    elif (answer == "add students"):
        try:
            answer2 = (input("student name"))
            answer3 = int(input("student height"))
            answer4 = (input("student gender"))
        except ValueError:
            print("stop being stupid")
        if (len(listy2) > 0):
            answer = listy2[0]
            listy[answer - 1] = student(answer4,answer3,answer2,id)
            listy2.remove[answer]
        else:
            listy.append(id)
            listy[id - 1] = student(answer2,answer3,answer4,id)
            id += 1
    elif (answer == "remove students"):
        try:
            answer2 = (input("student name"))
        except ValueError:
            print("stop being stupid")
        check = 0
        for i in range(0,len(listy)):
            checking = listy[check].name
            if (listy[check].name == answer2):
                del listy[check]
                sort()
                break

            check += 1
    elif (answer == "stop all"):
        looping = False

