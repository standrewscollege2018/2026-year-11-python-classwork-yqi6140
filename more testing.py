for i in range(1,1000):
    if (i%3 == 0):
        fizz = True
    else:
        fizz = False
    if (i%5 == 0):
        buss = True
    else:
        buss = True
    if(fizz == True and buss == True):
        print("fizzbuss")
    elif (fizz == True):
        print("fizz")
    elif (buss == True):
        print("buss")
    else:
        print(i)


