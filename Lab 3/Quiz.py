print("This is a simple 5-question quiz")

correct = 0
answer = int(input("What is 1+1:"))
if answer == 2:
    correct += 1
    print ("Correct!")
else:
    print ("Incorrect.")

answer = int(input("What is 3 * 2 - 1:"))
if answer == 5:
    correct += 1
    print ("Correct!")
else:
    print ("Incorrect.")

answer = input("What month is Christmas in? ")
if answer.lower() == "december":
    correct += 1
    print ("Correct!")
else:
    print ("Incorrect.")

answer = int(input("What is the best year to be born in?\n1. 1993\n2. 2000\n3. 2022\n4. 2047\nEnter choice:"))
if answer == 1:
    correct += 1
    print ("Correct!")
else:
    print ("Incorrect.")

answer = int(input("Who was the president in 2022?\n1. George Washington\n2. George Bush\n3. Donald Trump\n4. Joe Biden\nEnter choice:"))
if answer == 4:
    correct += 1
    print ("Correct!")
else:
    print ("Incorrect.")

print("Congradulations, you got %s correct" %correct)
print("That is a score of %s percet" %((correct / 5) * 100))