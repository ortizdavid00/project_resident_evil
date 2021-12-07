import random

# Available characters to choose from
characters = ["Leon S. Kennedy", "Claire Redfield"]
user_items = []

# Game Over Screen
def game_over():
    print("")
    print("You are Dead...")
    print("")
    restart_game() # Once player is killed, restart_game() function is called.

# Restart Game. Function linked to the game_over() function
def restart_game():
    while True:
        restart_input = input("Play again? Y/N: ")
        if restart_input == "yes" or restart_input == "y":
            game_start()
        elif restart_input == "no" or restart_input == "n":
            print("")
            print("The nightmare consumed another victim...")
            exit()
        else:
            print("Enter a valid command!")
            break

# Function holding operation of the game
def game_start():

    # Story intro function to be played for either character selected
    def story_intro():
        print("")
        print("Leon, a police officer for the Raccon City Police Department, finds Claire alone running away from a man that is pale-looking and covered in blood. Leon grabs Claire and they rush into a nearby police vehicle. They drive away as fast as they can, only to realize there was a zombie on the hood of the car. Leon swerves in an attempt to get the zombie off the car, but ends up crashing into a semi-truck, causing Leon and Claire to be split up. The city is in flames and is abandoned, or at least that is what they thought. This is where the nightmare begins...")
        print("")

    # Function once player reaches and enters the police station
    def police_entrance():
        print("")
        print("The police station is a huge building, with a cathedral-like setting. There are two doors on either side of you. There is a Lady Justice statue in the middle of the building in front of the double-sided staircase. There is a door on top of the staircase. I can either walk left, right or forward. It looks like this is where the true nightmare begins...")
        doors = [1, 2, 3]
        # Door choices in police station are random each playthrough. No option is the same per playthrough.
        def random_door():
            if random.choice(doors) == 1:
                print("The door was a trap and killed you instantly.")
                game_over()
            elif random.choice(doors) == 2:
                print("You approach the door and it is unlocked. You enter through the door and see a hallway and two zombies looking the other way...")
                print("")
                print("Thank you for you playing! The development of the nightmare continues...")
                restart_game()
            elif random.choice(doors) == 3:
                print("")
                print("You approach the door and it is unlocked. There are crows picking at a dead humans body. It looks like there is something shiny on his body...")
                print("")
                print("Thank you for you playing! The development of the nightmare continues...")
                restart_game()
        while True:
            door_choice = input("Enter your command: ")
            if door_choice == "walk forward" or door_choice == "walk left" or door_choice == "walk right":
                random.choice(doors)
                random_door()
            elif door_choice == "walk backwards":
                print("I shouldn't go back outside. It seems safer in here...")
                break
            else:
                print("Enter a valid command!")
                continue

    # Loop to play game. Launches title screen
    while True:
        print("")
        print("*-------------------------------------------*")
        print("|*******************************************|")
        print("|*************                 *************|")
        print("|************* Resident Evil 2 *************|")
        print("|*************                 *************|")
        print("|*******************************************|")
        print("*-------------------------------------------*")
        print("")

        # Main menu commands
        main_menu = input("1) Game Start\n2) Command List\n3) Exit Game\n").lower()
        print("")
        # Main menu if/elif/else statements for selecting options
        if main_menu == "1" or main_menu == "game start":
            char_select = input("Select your character:\n1) Leon S. Kennedy\n2) Claire Redfield\n").lower()
            print("")
            if char_select == "1" or char_select == "leon":
                user_char = characters[0]
                print("Player Selected:", characters[0])
                story_intro()
            elif char_select == "2" or char_select == "claire":
                user_char = characters[1]
                print("Player Selected:", characters[1])
                story_intro()
            else:
                print("Enter a valid command!")
                continue
            break
        # Prints command list for user
        elif main_menu == "2" or main_menu == "command list":
            print("These commands are commands to make your character walk/move, attack, and interact with their surrounding objects. Commands must be entered with the correct spelling, but are not case sensitive.\n1) Walk Forward\n2) Walk Backwards\n3) Walk Left\n4) Walk Right\n5) Attack\n6) Run away\n7) Interact\n8) Yes (Y)\n9) No (N)")
        # Exits game completely
        elif main_menu == "3" or main_menu == "exit game":
            print("The nightmare continues...")
            exit()
        # User validation for input
        else:
            print("Enter a valid command!")
            continue
    print(user_char, "finds themselves in the middle of a street, surrounded by burning cars, dead humans, and crows watching their every move. There is no way of turning back now...")

    # Loop for gameplay start
    def command_start():
        # Character HP
        char_hp = 500

        # Loop for the starting point. Different paths are available to player
        while True:
            first_command = input("You are at the starting point. Enter your command: ").lower()
            print("")
            # If/Elif statements to compare user input
            if first_command == "walk backwards":
                print("There is a burning semi-truck behind you. There is no escape...")
                continue
            elif first_command == "walk left":
                print("There is a dead police officer. The body is searchable for items.")
                while True:
                    gun_command = input("Will you search the body? Y/N: ").lower()
                    print("")
                    # Checks if player has already inspected body before
                    if gun_command == "yes" or gun_command == "y":
                        if "handgun" in user_items:
                            print("There is nothing else to grab...")
                            break
                        else:
                            print(user_char, "now has a 9mm handgun.")
                            user_items.append("handgun")
                            break
                    elif gun_command == "no" or gun_command == "n":
                        print("The dead body remains on the ground...")
                        break
                    else:
                        print("Enter a valid command!")
                        print("")
                        continue
            elif first_command == "walk right":
                print("There is an unlocked door. You open the door and see an office room, ripped papers lining the floor, only to see a zombie eating a human.")
                while True:
                    first_fight_command = input("Enter your command: ").lower()
                    print("")
                    if first_fight_command == "attack":
                        # Checks if a weapon is in player's inventory. Changes result of battle if so.
                        if "handgun" in user_items:
                            print(user_char, "killed the zombie! The path is clear to continue.")
                            break
                        else:
                            char_hp -= 100
                            print(user_char, "attempted to fight the zombie with their bare hands. The zombie died after a struggle, but", user_char, "is in pain.")
                            print(user_char, "now has", char_hp, "hp.")
                            break
                    elif first_fight_command == "run away":
                        print(user_char, "escaped the fight without losing any health. A weapon would really help...")
                        break
                    else:
                        print("Enter a valid command!")
                        print("")
                        continue
                # Checks if the first_fight command is attack. Will procede character to the next room.
                while first_fight_command == "attack":
                    print("")
                    print("There are no more dead zombies in the room. I wonder if there's something of use to find in this room...")
                    print("")
                    while True:
                        room_search = input("You are in the office room. Enter your command: ").lower()
                        # If/Elif statements to compare user input
                        if room_search == "walk forward":
                            print("There is a desk with drawers. Maybe there is something in these drawers...")
                            desk_search = input("Will you search the desk? Y/N: ").lower()
                            print("")
                            if desk_search == "yes" or desk_search == "y":
                                # Checks if police key is in user's inventory. Appends to inventory list.
                                if "police key" in user_items:
                                    print("There is nothing else to grab...")
                                    break
                                else:
                                    print(user_char, "now has a police key.")
                                    user_items.append("police key")
                                    break
                            elif desk_search == "no" or desk_search == "n":
                                print("The desk remains untouched...")
                                break
                            else:
                                print("Enter a valid command!")
                                print("")
                                continue
                        elif room_search == "walk left":
                            print("")
                            print("There is a broken photo of a family on the wall. Hope that family made it out alive...")
                            break
                        elif room_search == "walk right":
                            print("")
                            print("You see a dirty, cloudy window with a faint view of Raccoon City burning around you. The window is very hard to see out of, but there is a horde of zombies approaching the window that", user_char, "doesn't notice. The zombies break through and attack furiously.")
                            print("")
                            print(user_char, "has been eaten by the hoard of zombies!")
                            char_hp = 0
                            print(user_char, "now has", char_hp, "HP.")
                            game_over() # Game over function called once player is killed
                        elif room_search == "walk backwards":
                            print("")
                            print("You run out the door. You are now back in the starting position.")
                            command_start() # Calls the command_start function to bring the player back to the starting point.
                        else:
                            print("Enter a valid command!")
                            print("")
                            continue

            elif first_command == "walk forward":
                print("The Raccoon City Police Department station is in front of you. The big, wooden doors are closed shut, but it looks like there is a keyhole that isn't jammed...")
                print("")
                while True:
                    door_entrance = input("Enter your command: ").lower()
                    # Interact input checks if police key is in user_items lists.
                    if door_entrance == "interact":
                        if "police key" in user_items:
                            print("The police key might work for these wooden doors...")
                            door_interact = input("Enter your command: ").lower()
                            print("")
                            # Removes item from list and calls police_entrance() function.
                            if door_interact == "interact":
                                user_items.remove("police key")
                                print(user_char, "used the police key. The key turned with ease with an audible click. The door is now open and you proceed into the police station.")
                                print("The police key was removed from your inventory.")
                                police_entrance()
                        else:
                            print("Maybe searching for a key would help opening up these doors...")
                            break
                    elif door_entrance == "walk backwards":
                        break
                    else:
                        print("Enter a valid command!")
                        print("")
                        continue

    command_start()

game_start()