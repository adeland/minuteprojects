#Function to inform user of the game plot and commands.
def initial():
    print("Welcome to Marlene's Castle")
    print("Traverse the demon lord Marlene's castle to find treasure. Make sure you don't \nrun into Marlene!")
    print("Collect all the treasure to win; else incur Marlene's wrath.")
    print("Move commands are: North, West, South, and East.")
    print("Input commands are: Yes and No")

#Class object for rooms.
class Room:
    item = None
    riddle = None
    villainHere = None
    northRoom = None
    westRoom = None
    southRoom = None
    eastRoom = None
    solvedRoom = None
    roomNumber = None

    def __init__(self, roomNumber, item, riddle, villainHere = False, solvedRoom = False):
        self.item = item
        self.riddle = riddle
        self.villainHere = villainHere
        self.solvedRoom = solvedRoom
        self.roomNumber = roomNumber

#All room descriptions assigned to room variables.    
room1 = Room(1, "none", "", villainHere = False, )
room2 = Room(2, "old boots", "There is a gnome in the middle of the room, he asks: \nWhen Grant was 8, his brother was half his age. Now, Grant is 14. How old is his brother?")
room3 = Room(3, "wisdom scroll of basic mathematics", "There is a treant in the middle of the room \nit asks: What has a lot of teeth but can't bite?" )
room4 = Room(4, "stuffed doll", "There is a creepy stuffed doll on the floor, you pick it up.")
room5 = Room(5, "sword of stabbing", "An ornate silver sword laying on the ground, you pick it up")
room6 = Room(6, "none2", "A roar resounds through the room, the demon lord Marlene stands menacingly in front of you.", villainHere = True)
room7 = Room(7, "treasure chest", "There is an old wooden treasure chest in the center of the room. \nYou open it and pocketed some gold coins")
room8 = Room(8, "diamond necklace", "An shining diamond necklace is laying on the floor, you pick it up")

#All possible movements for room depending on what room you are in.
room1.northRoom = room2
room1.eastRoom = room7
room2.northRoom = room4
room2.westRoom = room3
room2.southRoom = room1
room2.eastRoom = room8
room3.eastRoom = room2
room4.southRoom = room2
room4.eastRoom = room5
room5.westRoom = room4
room6.southRoom = room8
room7.westRoom = room1
room8.northRoom = room6
room8.westRoom = room2

#List of items you can obtain throughout the game.
items = ["wisdom scroll of basic mathematics", "treasure chest", "sword of stabbing", "diamond necklace", "stuffed doll", "old boots", "none", "none2"]
y = ["none2"]

#Function for moving through rooms.
def move(room):
    print("You are now in room " + str(room.roomNumber))
    #If you have obtained the sword and encounter the villain, you can defeat the villain and win the game. Victory possibility #1.
    if "sword of stabbing" not in items and room.roomNumber == 6:
        print("You fight Marlene with the sword, striking her down! Victory!")
        quit()
    #If you encounter the villain and have not obtained the sword, the villain defeats you.
    if room.roomNumber == 6 and ('sword of stabbing' in items):
        print("You encounter the menacing demon lord Marlene. She roars and stomps on you. Game Over.")
        quit()
    #If you obtain all the items and avoid the villain room, you win. Victory possibility #2.
    if items == y and room.roomNumber == 1:
        print("You have escaped with the treasures, Victory!")
        quit()
    #If you go back and have already went into the room and aquired the item.
    if room.item not in items:
        print("You've been in this room before")
    else:
        print(room.riddle)
    #Riddles for room 3 and 4. If user input is correct, user obtains items. If incorrect user loses the game.
        if room.roomNumber == 2:
            ans = input()
            if ans == "10":
                print("Prince the gnome squeaks, \nCorrect!\nand hands you an old pair of boots.")
            else:
                print("Prince the gnome screams:\n INCORRECT! \n and bashes your skull in with his hammer. Game Over.")
                quit()
        elif room.roomNumber == 3:
            ans = input()
            comb = ("Comb, comb")
            if ans in comb:
                print("The treant growls: \n Correct, you may proceed, and hands you the scroll of basic mathematics")
            else:
                print("The treant opens up a hole beneath you. Game Over.")
                quit()
        #If item is aquired, removes item off item list.
        items.remove(room.item)
    #Loop to check what rooms are open    
    nextRoom = None
    while not nextRoom:
        nextdir = str(input("Where would you like to go next? "))
        if nextdir == "North" and room.northRoom:
            nextRoom = room.northRoom
        elif nextdir == "West" and room.westRoom:
            nextRoom = room.westRoom
        elif nextdir == "South" and room.southRoom:
            nextRoom = room.southRoom
        elif nextdir == "East" and room.eastRoom:
            nextRoom = room.eastRoom
        #If user inputs invalid room, tells user that there is no room there.
        else:
            print("There is no room that way, try again")
    move(nextRoom)
#Initializes script. if user doesnt want to enter the game, exits game.
if __name__ == '__main__':
    initial()
    x = str(input("You are at the front entrance, do you want to enter?"))
    if x == "Yes":
        move(room1)
    else:
        print("Okay, boring.")
        print("Game Over.")
        quit()
