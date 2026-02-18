number_of_time = 0
answer = 0
average = 0
while (answer != 1000):
    answer = int(input("what is your score type 1000 to end"))
    number_of_time += 1
average = answer/number_of_time
print(average)