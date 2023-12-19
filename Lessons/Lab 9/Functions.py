import random

def min3 (x, y, z):
    if x < y and x < z:
        return x
    if y < x and y < z:
        return y
    if z < x and z < y:
        return z
    if z == x and z == y:
        return z

# print(min3(4, 7, 5))
# print(min3(4, 5, 5))
# print(min3(4, 4, 4))
# print(min3(-2, -6, -100))
# print(min3("Z", "B", "A"))

def box(x, y):
    for i in range(x):
        for j in range(y):
            print("*", end="")
        print()

# box(7,5)  # Print a box 7 high, 5 across
# print()   # Blank line
# box(3,2)  # Print a box 3 high, 2 across
# print()   # Blank line
# box(3,10) # Print a box 3 high, 10 across

def find(list, x):
    for i in range(len(list)):
        if list[i] == x:
            print("Found %s at position %s" %(x, i))

# my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
# find(my_list, 12)
# find(my_list, 91)
# find(my_list, 80)
            
def create_list(x):
    created_list = []
    for i in range(x):
        created_list.append(random.randrange(1,7))
    return created_list

# my_list = create_list(5)
# print(my_list)

def count_list(list, x):
    countn = 0
    temp = set(list)
    countn = list.count(x)
    return countn

# count = count_list([1,2,3,3,3,4,2,1],3)
# print(count)

def average_list(list):
    average = 0
    for i in range(len(list)):
        average += list[i]
    return (average / len(list))

# avg = average_list([1,2,3])
# print(avg)

def main():
    my_list = create_list(10000)
    for i in range(1, 7):
        print(count_list(my_list, i))
    print(average_list(my_list))
if __name__ == "__main__":
    main()