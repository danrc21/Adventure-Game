import time
import random
import sys


def typewriter_simulator(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.07)
        else:
            time.sleep(1)


def print_pause(message, delay=.1):
    typewriter_simulator(message)
    time.sleep(delay)


def intro():
    print_pause("You arrive for your first day of work"
                " as a Building Engineer.\n")
    print_pause("Rumor has it that this building has multiple"
                " issues that terrify the tenants and employees.\n")
    print_pause("You open the doors to the building,"
                " empty handed.\n")


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        print_pause("Invalid response. Try again!\n")


def floor_1(items, issues):
    print_pause("You are in the lobby.\n")
    print_pause("To your left is the elevator.\n")
    if "access card" in items:
        print_pause("You see people walking in and out of the building.\n")
        print_pause("The security officer has already given"
                    " you an access card.\n")
        print_pause("There is nothing more to do here.\n")
        print_pause("You head to the elevator.\n")
        elevator(items, issues)
    else:
        print_pause("In front of you is the security desk.\n")
        response = valid_input("What would you like to do?\n"
                               "Enter 1 to go to the security desk.\n"
                               "Enter 2 to go to the elevator.\n",
                               ["1", "2"])
        if response == "1":
            security_desk(items, issues)
        elif response == "2":
            elevator(items, issues)


def security_desk(items, issues):
    print_pause("You approach the security desk.\n")
    print_pause("The security officer greets you"
                " and hands you an access card.\n")
    print_pause("You will need to go to floor 2.\n")
    items.append("access card")
    print_pause("You head to the elevator.\n")
    elevator(items, issues)


def elevator(items, issues):
    print_pause("You are in the elevator.\n")
    while True:
        response = valid_input("Where would you like to go?\n"
                               "Enter 1 for floor 1, Lobby\n"
                               "Enter 2 for floor 2, Engineer's Office\n"
                               "Enter 3 for floor 3, Business\n",
                               ["1", "2", "3"])
        if response == "1":
            floor_1(items, issues)
        elif response == "2":
            floor_2(items, issues)
        elif response == "3":
            floor_3(items, issues)


def floor_2(items, issues):
    print_pause("You have arrived on floor 2.\n")
    print_pause("The door to the Engineers office is in front of you.\n")
    print_pause("The Chief Engineer comes through the door and greets you.\n")
    if "access card" in items:
        print_pause("He asks you to test your access card.\n")
        print_pause("You use your access card to enter.\n")
        print_pause("The Chief Engineer introduces"
                    " you to the team.\n")
        print_pause("You meet everyone."
                    " You are given engineers tools!\n")
        print_pause("You are now ready for work!\n")
        print_pause("The Chief Engineer tells you to inspect"
                    " the floors for any " + issues + " that may occur.\n")
        items.append("engineers tools")

    else:
        print_pause("He notices you do not have an access card.\n")
        print_pause("The Chief Engineer tells you to speak to security.\n")
    print_pause("You head to the elevator.\n")
    elevator(items, issues)


def floor_3(items, issues):
    print_pause("You have arrived on floor 3.\n")
    print_pause("There is a door in front of you."
                " Suddenly it opens.\n")
    if "access card" in items:
        print_pause("The head of Business comes rushing out.\n")
        print_pause("She starts yelling." " There's an emergency,"
                    " a " + issues + " is happening on this floor!\n")
        while True:
            response = valid_input("Would you like to resolve the "
                                   + issues + "?\n"
                                   "Enter 1 to attempt to resolve "
                                   + issues + ".\n"
                                   "Enter 2 to go get help.\n", ["1", "2"])
            if response == "1":
                if "engineers tools" not in items:
                    if issues == "fire":
                        print_pause("You are unprepared."
                                    " The " + issues + " has spread."
                                    " Burning everything on the floor.\n")
                        play_again()
                    else:
                        print_pause("You are unprepared. The issue has"
                                    " not been resolved in time.\n")
                        print_pause("You are fired! Game over!\n")
                        play_again()
                else:
                    print_pause("With your engineer tools in hand,"
                                " you resolve the " + issues + ".\n")
                    print_pause("Having resolved the " + issues +
                                " so quickly,"
                                " everyone is so happy with you.\n")
                    print_pause("Your team congrulates and"
                                " celebrate with you.\n")
                    print_pause("You win!\n")
                    play_again()
            elif response == "2":
                print_pause("You state that you will need to get help.\n")
                print_pause("You quickly rush out of the room.\n")
                print_pause("You head to the elevator.\n")
                elevator(items, issues)
            else:
                print_pause("Invalid input. Try again!\n")
    else:
        print_pause("The head of Business comes out to greet you.\n")
        print_pause("She notices that you do not have an acess card.\n")
        print_pause("She tells you to speak with security.\n")
    print_pause("You head to the elevator.\n")
    elevator(items, issues)


def play_again():
    response = valid_input("Would you like to play again? (y/n)\n", ["y", "n"])
    if response == "y":
        play_game()
    elif response == "n":
        exit()


def play_game():
    items = []
    issues = random.choice(["leaky pipe", "fire", "power outage"])
    intro()
    floor_1(items, issues)


if __name__ == '__main__':
    play_game()
