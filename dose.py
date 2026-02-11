# Calculate papacetamol dose based on age and weight
age = int(input("what is the child's age"))
weight = 0
recommand = 0
while True:
    if (age < 12 and age > 0):
        weight = int(input("what is the child's weight(kg)"))
        recommand = 10 * weight
    else:
        recommand = 1000
    if (age > 0 and weight < 200 and weight >2  or age > 11):
        print(f"I recommand you have {recommand} milligrams of tablets")
    else:
        print("invaid information please retry")
        break

