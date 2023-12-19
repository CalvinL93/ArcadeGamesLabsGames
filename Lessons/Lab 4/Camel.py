import random

print ("Welcome to Camel!")
print ("You have stolen a camel to make your way across the great Mobi desert.")
print ("The natives want their camel back and are chasing you down! Survive your")
print ("desert trek and outrun the natives.")

traveled = 0
traveledTotal = 0
natives = -20
tired = 0
thirst = 0
canteen = 5

quit = False
while not quit:
    print ("A. Drink from your canteen.")
    print ("B. Ahead moderate speed.")
    print ("C. Ahead full speed.")
    print ("D. Stop and rest.")
    print ("E. Status check.")
    print ("Q. Quit.")
    choice = input("Your choice? ")

    if choice.upper() == "Q":
        quit = True

    elif choice.upper() == "E":
        print ("Miles traveled: %s" %traveledTotal)
        print ("Drinks in canteen: %s" %canteen)
        print ("The natives are %s miles behind you." %natives)

    elif choice.upper() == "D":
        print ("The camel is happy")
        natives += random.randrange(7, 14)
        thirst = 0
        tired = 0

    elif choice.upper() == "C":
        traveled = random.randrange(10,20)
        thirst += 1
        tired += random.randrange(1,3)
        natives += random.randrange(7, 14)
        traveledTotal += traveled
        print ("You traveled %s miles." %traveled)

    elif choice.upper() == "B":
        traveled = random.randrange(5,12)
        thirst += 1
        tired += 1
        natives += random.randrange(7, 14)
        traveledTotal += traveled
        print ("You traveled %s miles." %traveled)

    elif choice.upper() == "A":
        if canteen > 0:
            canteen -= 1
            thirst = 0
        else:
            print ("No more water in canteen.")
    
    if thirst > 5:
        print ("You died of thirst! Game Over.")
        quit = True
    elif thirst > 3:
        print ("You are thirsty.")

    if tired > 8:
        print ("Your camel is dead. Game Over.")
        quit = True
    elif tired > 5:
        print ("Your camel is getting tired.")

    if natives >= traveledTotal:
        print ("The natives caught you, your dead. Game Over.")
        quit = True
    elif natives >= traveledTotal - 15:
        print ("The natives are getting close!")

    if traveledTotal >= 200:
        print ("You made it across the desert! You won!")
        quit = True

    if random.randrange(1, 20) == 1:
        print ("You found an oasis!")
        canteen = 5
        tired = 0
        thirst = 0

    print ("\n")