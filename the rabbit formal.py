answer = int(input("how many times"))
STARTING_NUMBER = 1
STARTING_PREVIOUS_NUMBER = 0
newnumber = 0
answer2 = (input("do you want to define the starting numbers your self"))
if(answer2.lower == "yes"):
    answer2 = int(input("starting pop"))
    STARTING_NUMBER = answer2
    answer2 = int(input("starting pop boost"))
    STARTING_PREVIOUS_NUMBER = answer2
number = STARTING_NUMBER
previous_number = STARTING_PREVIOUS_NUMBER
listing = []
result = ""
for i in range(0,answer):
    newnumber = number
    listing.append(number)
    number += previous_number
    previous_number = newnumber
result = "  ".join(str(listing))
print(result)



