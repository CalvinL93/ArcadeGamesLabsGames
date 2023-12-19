room_list = []
# N, E, S, W
room = ["You are in the living room. There is a passage to the East and to the South.\n", None, 1, 3, None]
room_list.append(room)

room = ["You are in the bedroom. There is a passage to the East, South, and West.\n", None, 2, 4, 0]
room_list.append(room)

room = ["You are in the bathroom. There is a passage to the West.\n", None, None, None, 1]
room_list.append(room)

room = ["You are in the kitchen. There is a passage to the North and the East.\n", 0, 4, None, None]
room_list.append(room)

room = ["You are in the dinning room. There is a passage to the North and the West.\n", 0, None, None, 3]
room_list.append(room)

current_room = 0

# print(room_list[current_room])

done = False

while not done:
    print()
    next_room = None

    print(room_list[current_room][0])
    direction = input("Which way would you like to go? ")

    if direction.lower() == "n" or direction.lower == "north":
        next_room = room_list[current_room][1]
    elif direction.lower() == "e" or direction.lower == "east":
        next_room = room_list[current_room][2]
    elif direction.lower() == "s" or direction.lower == "south":
        next_room = room_list[current_room][3]
    elif direction.lower() == "w" or direction.lower == "west":
        next_room = room_list[current_room][4]
    elif direction.lower() == "q" or direction.lower == "quit":
        done = True
    else:
        print("Incorrect input. Enter North, East, South, West, or Quit")

    if next_room == None and not done:
        print("You can't go that way.")
    else:
        current_room = next_room
        

    