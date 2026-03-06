import time
car_list = []
car_seats_list = []
car_availablely_list = []
car_names_list = []


def add_car_to_the_list(carname,carseats):
    car_list.append(carname)
    car_seats_list.append(carseats)
    car_availablely_list.append(True)
    car_names_list.append("none")
def setup():
    add_car_to_the_list("Suzuki Van",2)
    add_car_to_the_list("Toyota Corolla",4)
    add_car_to_the_list("Honda CRV",4)
    add_car_to_the_list("Suzuki Swift",4)
    add_car_to_the_list("Mitsubishi Airtrek",4)
    add_car_to_the_list("Nissan DC Ute",4)
    add_car_to_the_list("Toyota Previa",7)
    add_car_to_the_list("Toyota Hi Ace",12)
    add_car_to_the_list("Toyota Hi Ace",12)
setup()
answer = -1
ready = 0
while True in car_availablely_list:
    time.sleep(0.1)
    ready = 0
    
    for check in range(0,len(car_list)):
        if car_availablely_list[check] == True:
            print(f"{check + 1}. {car_list[check]} it has {car_seats_list[check]} seats")
        else:
            print(f"{check + 1}. {car_list[check]} it has {car_seats_list[check]} seats and is unavaible")
        check += 1
    
    get_selection = True
    while get_selection  == True:
        try:
            answer = int(input("please choose a car or press zero to exit."))

            get_selection = False
        except ValueError:
            print("you are suppose to press the number in front of the car")
    
    
    if answer > len(car_list) or answer < 0:
        print("not acceptable there isn't a car with that number")
    elif answer == 0:
        break
    elif car_availablely_list[answer - 1] == False:
        print("this car have already been picked")
    else:
        print(f"you have chosen {car_list[answer - 1]}")
        car_availablely_list[answer - 1] = False
        get_selection = True
        while get_selection  == True:
            try:
                new = (input("your name."))
                if new.strip() == "":
                    print("you cann't just put nothing")
                else:
                    get_selection = False
            except ValueError:
                print("not able")
        car_names_list[answer - 1] = new
    print(" ")
    
print("ending simulation")
for check in range(0,len(car_list)):
        if car_names_list[check] != "none":
            print(f"{check + 1}. {car_list[check]} it has {car_seats_list[check]} seats and has been taken by {car_names_list[check]}")
        else:
            print(f"{check + 1}. {car_list[check]} it has {car_seats_list[check]} seats and has not been taken")
        check += 1