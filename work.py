listy = ["John Ana","Spencer","Brosn","yang"]
listy2 = ["no","yes","yes","no"]
finished = False
number = 0
print(listy)
while (finished == False):
    try:
        number = int(input(f"pick 1 to {len(listy)} press 0 to stop "))
    except:
        print("stop being stupid")
    if (number == 0):
        finished = True
    if (number > 0):
        print(listy[number - 1])
        print(listy2[number - 1])